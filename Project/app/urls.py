from django.urls import path
from .views import AuthAPIView, UserAddAPIView, UserListAPIView, UserEditAPIView

urlpatterns = [
    path('auth/', AuthAPIView.as_view(), name='auth'),
    path('user/add/', UserAddAPIView.as_view(), name='user-add'),
    path('user/list/', UserListAPIView.as_view(), name='user-list'),
    path('user/edit/<int:pk>/', UserEditAPIView.as_view(), name='user-edit'),
]