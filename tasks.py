from celery_worker import celery
import time
import datetime

@celery.task
def send_email_task(email: str):
    print("-----------Start---------------------:" , datetime.datetime.now())
    time.sleep(25)
    print("-----------End-----------------------:", datetime.datetime.now())
    print(f"Email sent to {email}")
    return "Done"
