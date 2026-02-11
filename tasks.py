from celery_worker import celery
import time
import datetime

@celery.task
def send_email_task(email: str):
    print("-----------Start---------------------:" , datetime.datetime.now())
    time.sleep(5)
    print("-----------End-----------------------:", datetime.datetime.now())
    print(f"Email sent to {email}")
    return (f"Email sent to {email}")

@celery.task
def heavy_calculation_task(number: int):
    print("Starting heavy calculation..................")
    total = 0
    for i in range(10_000_000):
        total += i
    return f"Calculation done for {number}"

@celery.task
def process_file_task(filename: str):
    print(f"Processing file {filename}")
    time.sleep(15)
    return f"{filename} processed successfully........."
