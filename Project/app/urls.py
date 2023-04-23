from django.urls import path
from .views import AuthAPIView, UserAddAPIView, UserListAPIView, UserEditAPIView

urlpatterns = [
    path('api/1.0/auth/', AuthAPIView.as_view(), name='auth'),
    path('api/1.0/user/add/', UserAddAPIView.as_view(), name='user-add'),
    path('api/1.0/user/list/', UserListAPIView.as_view(), name='user-list'),
    path('api/1.0/user/edit/<int:pk>/', UserEditAPIView.as_view(), name='user-edit'),
]