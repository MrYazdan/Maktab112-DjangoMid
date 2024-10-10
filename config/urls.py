from django.contrib import admin
from django.urls import path
from apps.book.views import BookListCreateAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books', BookListCreateAPIView.as_view(), name="book_list_create")
]
