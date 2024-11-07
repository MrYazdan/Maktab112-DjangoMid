from django.core.exceptions import ValidationError
from django.db import models

from .models import User

from services.mail import MailProvider
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete, m2m_changed, class_prepared


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        _ = MailProvider(
            "Welcome",
            instance.email,
            "mail/welcome.html",
        ).send()


@receiver(pre_delete, sender=User)
def prevent_admin_delete(sender, instance, **kwargs):
    if instance.is_superuser:
        raise ValidationError("Cannot delete admin (super user) user !")


@receiver(m2m_changed, sender=User.friends.through)
def log_friend_added(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        for friend_id in pk_set:
            print(f"{instance.email} added friend with id {friend_id}")


@receiver(class_prepared)
def add_dynamic_field(sender, **kwargs):
    if sender.__name__ == "FakeUser":
        print("🖐🏻 -- 🖐🏻")
        sender.add_to_class("is_online", models.BooleanField(default=False))