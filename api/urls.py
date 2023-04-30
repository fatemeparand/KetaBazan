from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.ApiBookList.as_view(), name='api_book_list'),
    path('<int:pk>/', views.ApiBookDetail.as_view(), name='api_book_detail'),
    path('users/', views.ApiUserList.as_view(), name='api_user_list'),
    path('users/<int:pk>', views.ApiUserDetail.as_view(), name='api_user_detail'),
]
