from django import forms
from .models import Book, Comment
from django.utils.translation import gettext_lazy as _


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
                  'image',
                  ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', ]

