from django.db.utils import IntegrityError
from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookTestCase(TestCase):
    def test_create_book(self):
        # book = Book.objects.create(title="Ajab maktabi darim ma", price=1000)
        #
        # self.assertEqual(book.is_deleted, False)
        # response = self.client.get(reverse("book_list_create"))
        #
        # print(response.content)
        #
        # self.assertContains(response, "Ajab maktabi darim ma")
        pass

    def test_create_book_tdd(self):
        book = Book.objects.create(title="title")

        self.assertEqual(book.is_deleted, False)
        # self.assertEqual(book.is_active, True)
        self.assertIsInstance(book.price, int)
        self.assertGreaterEqual(book.price, 0)

        with self.assertRaises(IntegrityError):
            Book.objects.create()
            Book.objects.create(title="title")
            Book.objects.create(price=20000)





