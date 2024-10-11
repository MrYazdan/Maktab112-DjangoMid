from random import randint
from django.shortcuts import render
from django.core.cache import cache


def sample(request):
    if not (data := cache.get("sample")):
        data = randint(100, 900)
        cache.set("sample", data, 30)

    print(data)
    return render(request, "sample.html", context=dict(numbers=range(1_000)))
