from django.shortcuts import render, get_object_or_404

from .models import Book


def book_list(request):
    book_lists = Book.objects.filter(active=True).order_by('-datetime_modified')
    context = {'book_lists': book_lists}
    return render(request, 'bookstore/book_list.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    content = {'book': book}

    return render(request, 'bookstore/book_detail.html', content)
