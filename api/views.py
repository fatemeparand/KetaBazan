from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from bookstore.models import Book
from .serializers import BookSerializer, BookDetailSerializer, UserSerializer,UserDetailSerializer
from accounts.models import CustomUser


class ApiBookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ApiBookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


class ApiUserList(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ApiUserDetail(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
