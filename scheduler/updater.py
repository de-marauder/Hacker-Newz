from apscheduler.schedulers.background import BackgroundScheduler
from . import newsAPI

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(newsAPI.update_news, 'interval', minutes=5)
    scheduler.start()
    print('scheduler loaded...')