from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookCreationForm
from .models import Book


def book_list(request):
    book_lists = Book.objects.filter(active=True).order_by('-datetime_modified')
    context = {'book_lists': book_lists}
    return render(request, 'bookstore/book_list.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    content = {'book': book}

    return render(request, 'bookstore/book_detail.html', content)


def book_create(request):
    if request.method == 'POST':
        form = BookCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookstore:book_list')

    else:
        form = BookCreationForm()

    context = {'form': form}
    return render(request, 'bookstore/book_create.html', context)


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookCreationForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect(book.get_absolute_url())

    context = {'form': form}
    return render(request, 'bookstore/book_create.html', context)
