from rest_framework import serializers
from bookstore.models import Book
from django.contrib.auth import get_user_model


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'book_name', 'book_author', 'book_price')


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ('datetime_created', 'datetime_modified')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'is_staff')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
