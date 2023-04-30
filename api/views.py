from rest_framework.generics import ListAPIView
from bookstore.models import Book
from .serializers import BookSerializer


class ApiBookList(ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer



