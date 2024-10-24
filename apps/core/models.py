from django.db import models
from apps.core.managers import LogicalManager
from django.contrib.auth import get_user_model, user_logged_in

User = get_user_model()


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LogicalDeleteMixin(models.Model):
    is_deleted = models.BooleanField(default=False)

    objects = LogicalManager()

    def delete(self, using=None, keep_parents=False):
        if not self.is_deleted:
            self.is_deleted = True
            self.save(update_fields=["is_deleted"])

    # base_manager = models.Manager()

    class Meta:
        abstract = True


class DailyVisit(models.Model):
    url = models.CharField(max_length=255)
    date = models.DateField()
    count = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = "url", "date"


class ActivityManager(models.Manager):
    def db_manager(self, using="activity", hints=None):
        return super().db_manager(using, hints)

    def using(self, alias="activity"):
        return super().using(alias)


class UserActivity(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, default=None, editable=False)
    ip = models.GenericIPAddressField(editable=False)
    url = models.CharField(max_length=255, editable=False)

    objects = ActivityManager()

    @property
    def timestamp_at(self):
        return self.timestamp.strftime("%Y/%m/%d  - %H:%M:%S")

