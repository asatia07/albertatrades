import logging
from lib import indeed_api
from indeed import models
from django_cron import CronJobBase, Schedule

logger = logging.getLogger(__name__)

class UpdateTradesJob(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'indeed.update_trades_cron_job'    # a unique code

    def do(self):
        trades = models.Trade.objects.all()
        for trade in trades:
            params = {'query': trade.query}
            response = indeed_api.fetch_jobs(params, job_count=True)
            if response["error"]:
                print response["message"]
                logger.error(response["message"])
            else:
                trade_info = response["trade_info"]
                job_counts = trade_info["totalResults"]
                models.Trade.objects.filter(query=trade.query).update(job_counts=job_counts)
                msg = "Job count updated for %s trade" %(trade.query)
                logger.info(msg)