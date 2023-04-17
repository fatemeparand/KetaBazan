from django.urls import path
from . import views

app_name = 'bookstore'


urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('new-book/', views.book_create, name='book_create'),
]
