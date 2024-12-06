from django.core.management.base import BaseCommand
from django_celery_beat.models import CrontabSchedule, PeriodicTask


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        schedule, created = CrontabSchedule.objects.get_or_create(
            minute="0",
            hour="0",
            day_of_week="*",
            day_of_month="*",
            month_of_year="*"
        )

        PeriodicTask.objects.update_or_create(
            name="Generate daily activity report",
            defaults={
                "task": "core.tasks.send_daily_activities",
                "crontab": schedule,
                "args": "[]",
                "kwargs": "{}",
            }
        )


