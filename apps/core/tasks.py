import json
from datetime import timedelta
from celery import shared_task
from django.core import serializers
from django.core.mail import EmailMessage
from django.db import transaction
from django.utils import timezone
from apps.core.models import UserActivity


@shared_task(bind=True, max_retries=3)
def send_daily_activities(self):
    try:
        yesterday = timezone.now() - timedelta(days=1)
        activities = UserActivity.objects.filter(timestamp__date=yesterday.date())

        if not activities.exists():
            return "No activity found for the day !"

        serialized_obj = serializers.serialize('json', activities)
        file_path = f"tmp/{yesterday.date()}.json"

        with open(file_path, "w") as json_file:
            json.dump(serialized_obj, json_file)

        email = EmailMessage(
            subject="Daily User Activity Report",
            body="attached json file report ...",
            from_email="developer@site.dev",
            to=["management@site.dev"],
        )
        email.attach(file_path, content="application/json")
        email.send()

        with transaction.atomic():
            activities.delete()

        return "Report successfully send to management ..."
    except Exception as e:
        print("Error:", e)
        # if self.request.retries >= self.max_retries:
        #     print("Failed to send report .")
        # raise self.retry(exc=e, countdown=15 * 60)