from django.contrib import admin
from django.urls import path, include

from apps.accounts.views import sample
from apps.book.views import BookListCreateAPIView


urlpatterns = [
    path("", include("apps.accounts.urls")),
    path('admin/', admin.site.urls),
    path('sample/', sample, name="sample"),
    path('api/books', BookListCreateAPIView.as_view(), name="book_list_create")
]
