from time import sleep
from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .serializers import BookSerializer, Book


# caching (func-based):
@cache_page(60 * 60)
def sample_functional_view(requests):
    pass


@method_decorator(cache_page(30), name="dispatch")
class BookListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request, *args, **kwargs):
        sleep(5)
        print("Salam be hame !")
        return super().get(request, *args, **kwargs)
