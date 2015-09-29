import urllib
import json
import config
import logging

def fetch_jobs(params):
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

        response = urllib.urlopen( "%s%s" %(config.INDEED_API_BASE_URL, urllib.urlencode(query_params)) )
        response = {"error": False, "trade_info": json.load(response)}
    except:
        error_msg = "Error in fetching data for query = %s" %query
        response = {"error": True, "message": error_msg}
    return response
