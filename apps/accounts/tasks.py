from time import sleep
from celery import shared_task


@shared_task
def send_welcome_email(to):
    print(f"Sending mail to {to}")
    sleep(10)
    print(f"Email send to {to} !")
