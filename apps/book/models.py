from django.db import models
from django.core.validators import MinValueValidator

from apps.core.models import TimeStampMixin, LogicalDeleteMixin


class Author(TimeStampMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"<{self.id} - {self.name}>"


class Document(models.Model):
    title = models.CharField(max_length=180, blank=False)
    file = models.FileField()


class Book(TimeStampMixin, LogicalDeleteMixin):
    title = models.CharField(max_length=180, blank=False)
    published_date = models.DateField(null=True)
    price = models.FloatField(validators=[
        MinValueValidator(0)
    ])
    slug = models.SlugField(unique=True, blank=True)
    authors = models.ManyToManyField(Author, blank=True)
    is_available = models.BooleanField(default=True)
    categories = models.ManyToManyField("Category", blank=True)

    def __str__(self):
        return f"{self.id}"


class Category(TimeStampMixin):
    name = models.CharField(max_length=200, blank=False)
    parent = models.ForeignKey("self", related_name="children", on_delete=models.SET_NULL, default=None, null=True,
                               blank=True)

    def __str__(self):
        return f"{self.name}"
