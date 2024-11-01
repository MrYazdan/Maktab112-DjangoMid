from django.contrib import admin
from django.urls import path

from .views import Sign, Verify


urlpatterns = [
    path('auth/sign', Sign.as_view(), name="sign"),
    path('auth/verify', Verify.as_view(), name="verify"),
]
