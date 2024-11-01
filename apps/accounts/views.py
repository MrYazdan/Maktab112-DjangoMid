from random import randint

from django.contrib.auth import login
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.urls import reverse_lazy
from django.views import View

from apps.accounts.models import User
from services.mail import MailProvider


def sample(request):
    if not (data := cache.get("sample")):
        data = randint(100, 900)
        cache.set("sample", data, 30)

    print(data)
    return render(request, "sample.html", context=dict(numbers=range(1_000)))


class Sign(View):
    @staticmethod
    def code_generator():
        return str(randint(100000, 999999))

    def get(self, request, *args, **kwargs):
        return render(request, "sign.html")

    def post(self, request, *args, **kwargs):
        email = self.request.POST.get("email")
        assert email, "Email field must be set !"

        if not (code := cache.get(email)):
            code = self.code_generator()

        _ = MailProvider(
            "Login/Register CODE",
            email,
            "mail/code.html",
            {"code": code}
        ).send()

        cache.set(email, code, 180)
        return redirect(reverse_lazy("verify"))


class Verify(View):
    def get(self, request, *args, **kwargs):
        return render(request, "verify.html")

    def post(self, request, *args, **kwargs):
        email = self.request.POST.get("email")
        assert email, "Email field must be set !"

        code = self.request.POST.get("code")
        assert code, "Code field must be set !"

        if cache.get(email) != code:
            raise ValidationError("verification code has been expired !")

        user, created = User.objects.get_or_create(email=email)

        login(request, user)

        return redirect("/")





