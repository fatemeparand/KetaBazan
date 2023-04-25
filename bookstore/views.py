from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import BookCreationForm
from .models import Book


class BookList(generic.ListView):
    context_object_name = 'book_lists'
    template_name = 'bookstore/book_list.html'

    def get_queryset(self):
        return Book.objects.filter(active=True).order_by('-datetime_modified')


class BookDetail(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'bookstore/book_detail.html'


class BookCreate(LoginRequiredMixin, generic.CreateView):
    model = Book
    form_class = BookCreationForm
    context_object_name = 'form'
    template_name = 'bookstore/book_create.html'


class BookUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    form_class = BookCreationForm
    context_object_name = 'form'
    template_name = 'bookstore/book_create.html'

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class BookDelete(LoginRequiredMixin,UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = 'bookstore/book_delete.html'
    success_url = reverse_lazy('bookstore:book_list')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


# from django.contrib.auth.decorators import login_required
# def book_list(request):
#     book_lists = Book.objects.filter(active=True).order_by('-datetime_modified')
#     context = {'book_lists': book_lists}
#     return render(request, 'bookstore/book_list.html', context)


# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#
#     content = {'book': book}
#
#     return render(request, 'bookstore/book_detail.html', content)


# @login_required
# def book_create(request):
#     if request.method == 'POST':
#         form = BookCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('bookstore:book_list')
#
#     else:
#         form = BookCreationForm()
#
#     context = {'form': form}
#     return render(request, 'bookstore/book_create.html', context)

# @login_required
# def book_update(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     form = BookCreationForm(request.POST or None, instance=book)
#     if form.is_valid():
#         form.save()
#         return redirect(book.get_absolute_url())
#
#     context = {'form': form}
#     return render(request, 'bookstore/book_create.html', context)

# @login_required
# def book_delete(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         book.delete()
#         return redirect('bookstore:book_list')
#
#     context = {'book': book}
#     return render(request, 'bookstore/book_delete.html', context)
