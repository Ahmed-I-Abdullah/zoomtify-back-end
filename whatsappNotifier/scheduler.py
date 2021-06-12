from .whatsappApi import send_message
from datetime import datetime
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def schedule_message(receiver_number, date_time):
    scheduler = BlockingScheduler()
    # def my_job():
    #      send_message(receiver_number, date_time)
    def my_job():
         print("Message Sent!")
    date_time_obj = datetime.strptime(date_time, '%Y-%m-%dT%H:%M')
    job = scheduler.add_job(
        my_job
        , run_date=date_time_obj)

    scheduler.start()
