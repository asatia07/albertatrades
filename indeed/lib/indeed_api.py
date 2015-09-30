import urllib
import json
import config
import logging

def fetch_jobs(params, job_count=False):
    query = params.get('query')
    if not query:
        error_msg = "Error : query(trade) is mandatory!"
        response = {"error": True, "message": error_msg}
    try:    
        query_params = {
            'publisher': config.INDEED_PUBLISHER_ID, 
            'fromage': config.INDEED_JOBS_FROMAGE,
            'sort': params.get('sort') if params.get('sort') else config.INDEED_JOBS_DEFAULT_SORTING,
            'limit': params.get('limit') if params.get('limit') else config.INDEED_JOBS_DEFAULT_LIMIT,
            'co': params.get('country') if params.get('country') else config.INDEED_JOBS_DEFAULT_COUNTRY,
            'l': params.get('location') if params.get('location') else config.INDEED_JOBS_DEFAULT_LOCATION,
            'v': 2,
            'format': 'json',
            'q': query,
        }
        trade_info = []
        start = 0
        while(True):
            url = "%s%s&start=%s" %( config.INDEED_API_BASE_URL, urllib.urlencode(query_params), start)
            response = urllib.urlopen(url)
            result = json.load(response)
            if job_count:
                trade_info = result
                break

            trade_info.extend(result["results"])
            start = result["end"]
            if start == result["totalResults"]:
                break

        response = {"error": False, "trade_info": trade_info}
    except:
        error_msg = "Error in fetching data for query = %s" %query
        response = {"error": True, "message": error_msg}
    return response
