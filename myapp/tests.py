from django.test import TestCase
from .models import Book


class BookModelTest(TestCase):
    def test_book_category(self):
        book = Book.objects.create(title = 'book 1' , author = 'kosa')
        
        self.assertEqual(str(book) ,"book 1")