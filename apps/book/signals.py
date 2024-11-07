from django.utils.text import slugify

from .models import Book, Document

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete


@receiver(pre_save, sender=Book)
def set_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


@receiver(post_delete, sender=Document)
def delete_file(sender, instance, **kwargs):
    instance.file.delete(False)


