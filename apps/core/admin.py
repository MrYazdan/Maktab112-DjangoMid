from django.contrib import admin
from .models import DailyVisit, UserActivity

admin.site.register(
    DailyVisit,
    admin.ModelAdmin,
    list_display=["date", "url", "count"],
    readonly_fields=["date", "count", "url"]
)

admin.site.register(
    UserActivity,
    admin.ModelAdmin,
    list_display=["timestamp", "user", "ip", "url"],
    readonly_fields=["timestamp", "user", "ip", "url"]
)
