from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models import Q
from datetime import datetime
from lib import indeed_api, config
from indeed.models import Trade, UserProfile
from indeed.models import UserSearchHistory
from .forms import FeedbackForm

def home(request):
    prev_search_history = None
    if request.user:
        if request.user.id:
            prev_search_history = UserSearchHistory.objects.filter(user=request.user).exclude(Q(query__isnull=True) | Q(query__exact='')).order_by('-modified')[:5]

    trades = Trade.objects.exclude((Q(name__isnull=True) | Q(name__exact='')) & (Q(query__isnull=True) | Q(query__exact='')))
    return render(request, 'indeed/home.html', context={"trades":trades, "prev_search_history":prev_search_history})

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

@login_required(login_url='/accounts/login/')
def job_listing(request):
    user_profile = UserProfile.objects.filter(user=request.user)
    if user_profile:
        query = user_profile[0].search_query
        location = user_profile[0].search_location
        return HttpResponseRedirect("/search_indeed/?query=%s&location=%s" %(query, location))
    else:
        return HttpResponseRedirect("/accounts/profile")

def search(request):
    query = request.GET.get('query',"").strip()
    location = request.GET.get('location',"").strip()
    jobs = []
    if query and (not query.isspace()):
        if not location:
            location = config.INDEED_JOBS_DEFAULT_LOCATION
        create_search_history(request, query, location)
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
    context = {"jobs":jobs, "query":query, "location":location}
    return render(request, 'indeed/search.html', context=context)

def create_search_history(request, query, location):
    if request.user.is_authenticated():
        prev_search_history = UserSearchHistory.objects.filter(user=request.user).filter(location=location).filter(query=query).first()
        if prev_search_history:
            prev_search_history.query = query
            prev_search_history.location = location
        else:
            prev_search_history = UserSearchHistory(user=request.user, query=query, location=location)
        prev_search_history.save() 

        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_profile.search_query = query
        user_profile.search_location = location
        user_profile.save()
