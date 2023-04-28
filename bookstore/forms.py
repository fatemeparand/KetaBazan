from django import forms
from .models import Book


class BookCreationForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name',
                  'book_author',
                  'book_translator',
                  'book_publisher',
                  'publication_year',
                  'book_introduction',
                  'short_description',
                  'book_price',
                  'book_pages',
                  'subject',
                  'status',
                  'active',
                  'owner',
                  'book_cover',
                  ]


