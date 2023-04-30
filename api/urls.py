from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.ApiBookList.as_view(), name='api_book_list'),
    path('<int:pk>/', views.ApiBookDetail.as_view(), name='api_book_detail'),
]
