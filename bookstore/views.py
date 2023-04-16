from django.shortcuts import render
from .models import Book


def book_list(request):
    book_lists = Book.objects.all()
    context = {'book_lists': book_lists}
    return render(request, 'bookstore/book_list.html', context)
