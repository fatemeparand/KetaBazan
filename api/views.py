from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from bookstore.models import Book
from accounts.models import CustomUser
from .serializers import BookSerializer, BookDetailSerializer, UserSerializer,UserDetailSerializer
from .permissions import IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly


class ApiBookList(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.order_by('datetime_created')


class ApiBookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class ApiUserList(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)

    def get_queryset(self):
        return CustomUser.objects.order_by('date_joined')


class ApiUserDetail(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)
