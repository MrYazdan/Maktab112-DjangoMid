from rest_framework import generics

from .serializers import BookSerializer, Book


class BookListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
