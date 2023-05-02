from django.urls import path
from . import views

app_name = 'bookstore'


urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('new-book/', views.BookCreate.as_view(), name='book_create'),
    path('<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
    path('comment/<int:pk>/', views.CommentCreate.as_view(), name='comment_create'),
]
