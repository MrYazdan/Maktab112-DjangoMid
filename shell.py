import os
import django
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# logger = logging.getLogger('django.db.backends')
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

# from mixer.backend.django import mixer
# from apps.book.models import Author, Book, Category  # noqa:E402

# book = Book(title="The 1", price=10000)
# book.save()

# print(Book.objects.all())
# print(Book.objects.all())
# print(Book.objects.deleted())
# print(Book.objects.archive().filter(is_deleted=True))
# print(Book.objects.get(id=9).title)
# print(Book.objects.all())
# print(Book.objects.filter(id__gte=1))
# print("Deleted: ", Book.objects.deleted().undelete())
# print("All: ", Book.objects.all())

from apps.accounts.models import User
User.objects.create(email="ismr3@gmailpo.co")

# print(User.objects.all()[0])
# User.objects.create_superuser('yazdan', password="1")
# books = mixer.cycle(10).blend(Book)

# send mail:
# from django.core.mail import send_mail
# send_mail("subject of test mail", "this is message ...", "maktab@mryazdan.ir", recipient_list=[
#     "ismryazdan@gmail.com"
# ])
# from services.mail import MailProvider
# from time import time
#
# mail = MailProvider(
#     "Welcome",
#     "ismryazdan@gmail.com",
#     "mail/welcome.html",
# )
#
# start_time = time()
# mail.send()
# print(f"{time()-start_time}s")