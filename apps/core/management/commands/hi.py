from email.policy import default

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "➡ this is help of hi command"

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, help="name shoma :)")

    def handle(self, *args, **kwargs):
        self.stdout.write("Salam be rooye mahetoon 😁")
        self.stdout.write(f"Salam be {kwargs.get('--name', 'binam')} aziz")


