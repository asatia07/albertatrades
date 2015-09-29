from django.http import HttpResponse
from indeed import lib
from indeed import models

def update_trades(request):
    trades = models.Trade.objects.all()
    for trade in trades:
        params = {'query': trade.query}
        response = lib.indeed_api.fetch_jobs(params)
        if response["error"]:
            print response["message"]
        else:
            trade_info = response["trade_info"]
            job_counts = trade_info["totalResults"]
            models.Trade.objects.filter(query=trade.query).update(job_counts=job_counts)
        
    return HttpResponse("update trade's job-count done!")


