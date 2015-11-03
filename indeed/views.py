from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from lib import indeed_api, config
from indeed.models import Trade, UserProfile
from indeed.models import QuerySearchHistory
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import FeedbackForm
from datetime import datetime
from django.db.models import Q

def home(request):
    prev_search_history = None
    if request.user:
        if request.user.id:
            prev_search_history = QuerySearchHistory.objects.filter(user_id=request.user.id).exclude((Q(trade__name__isnull=True) | Q(trade__name__exact='')) & (Q(trade__query__isnull=True) | Q(trade__query__exact=''))).order_by('-modified')[:5]

    trades = Trade.objects.exclude((Q(name__isnull=True) | Q(name__exact='')) & (Q(query__isnull=True) | Q(query__exact='')))
    return render(request, 'indeed/home.html', context={"trades":trades, "prev_search_history":prev_search_history, "indeed_logo":True})

def feedback(request):
    if request.method == 'GET':
        form = FeedbackForm()
    elif request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            email_data = {'email':form.cleaned_data['email'], 'name':form.cleaned_data['name'], 'feedback':form.cleaned_data['feedback']}
            body = render_to_string('indeed/email/feedback.html', email_data)
            mail_sent = send_mail('AlbertaTrades Feedback', body, 'donotreply@vanbit.io',['info@vanbit.io'], fail_silently=True, html_message = body)
            if mail_sent:
                messages.success(request, "Success! your feedback has been sent!")
                return redirect(home)
            else:
                messages.error(request, "Something went wrong, feedback not sent!")
        else:
            print "INVALID FORM"
            print form.errors
    context = {"form":form}
    return render(request, 'indeed/feedback.html', context=context)

def job_listing(request):
    if request.user:
        if request.user.id:
            user_profile = UserProfile.objects.filter(user=request.user)
            if user_profile:
                query = user_profile[0].search_query
                location = user_profile[0].search_location
                return HttpResponseRedirect("/search_indeed/?query=%s&location=%s" %(query, location))
    return HttpResponseRedirect("/accounts/profile")

def search(request):
    location = request.GET.get('location')
    query = request.GET.get('query')
    jobs = []
    if query:
        create_search_history(request, query)
        params = {'query': query, 'location': location}
        response = indeed_api.fetch_jobs(params)
        if response["error"]:
            print response["message"]
        else:
            for row in response["trade_info"]:
                jobs.append(
                                {
                                    "title": row["jobtitle"],
                                    "company": row["company"],
                                    "city": row["city"],
                                    "state": row["state"],
                                    "country": row["country"],
                                    "date": row["date"],
                                    "url": row["url"],
                                    "formattedLocationFull": row["formattedLocationFull"],
                                    "formattedRelativeTime": row["formattedRelativeTime"],
                                }
                            )
    context = {"jobs":jobs, "query":query, "location":location, "indeed_logo":True}
    return render(request, 'indeed/search.html', context=context)

def create_search_history(request, query):
    location = request.GET.get('location') if request.GET.get('location') else config.INDEED_JOBS_DEFAULT_LOCATION
    trade, created = Trade.objects.get_or_create(name=query)
    if trade:
        if created:
            trade.query = query
            trade.location = location
            trade.save()

        if request.user.is_authenticated():
            user_id = request.user.id
            prev_search_history = QuerySearchHistory.objects.filter(user_id=user_id).filter(location=location).filter(trade=trade).first()
            if prev_search_history:
                prev_search_history.location = location
                prev_search_history.trade = trade
            else:
                prev_search_history = QuerySearchHistory(user_id=user_id, trade=trade, location=location)
            prev_search_history.save() 

            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            user_profile.search_query = query
            user_profile.search_location = location
            user_profile.save()
