from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from lib import indeed_api
from models import Trade
from models import QuerySearchHistory

def home(request):
    trades = Trade.objects.all()
    return render(request, 'indeed/home.html', context={"trades":trades, "indeed_logo":True})

def search(request):
    location = request.GET.get('location')
    query = request.GET.get('query')
    create_search_history(request, query)

    jobs = []
    if query:
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

    trade = Trade.objects.filter(name=query)
    if trade:
        user_id = request.user.id if (request.user and request.user.id)  else 0
        search_history = QuerySearchHistory(user_id=user_id, trade=trade[0])
        search_history.save()

        

