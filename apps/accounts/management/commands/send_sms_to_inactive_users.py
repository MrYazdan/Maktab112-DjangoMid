from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


User = get_user_model()


class Command(BaseCommand):
    help = "➡ this is help of send_sms_to_inactive_users command"

    def handle(self, *args, **kwargs):
        one_month_ago = timezone.now() - timedelta(days=30)
        inactive_users = User.objects.filter(last_login__lt=one_month_ago)

        for user in inactive_users:
            # send sms :)
            self.stdout.write(f"📨 Send sms to {user.phone}")
