from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AuthAPI, UserAddAPI, UserListAPI, UserEditAPI

urlpatterns = format_suffix_patterns([
    path('auth/', AuthAPI.as_view()),
    path('user/add/', UserAddAPI.as_view()),
    path('user/list/', UserListAPI.as_view()),
    path('user/edit/<int:pk>/', UserEditAPI.as_view()),
])