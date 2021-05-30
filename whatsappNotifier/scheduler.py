from .whatsappApi import send_message
from datetime import datetime
from apscheduler.scheduler import Scheduler

def schedule_message(sender_number, receiver_number, date_time):
    scheduler = Scheduler()
    scheduler.start()
    my_job = send_message(sender_number, receiver_number, date_time)
    job = scheduler.add_date_job(my_job, date_time)


    
