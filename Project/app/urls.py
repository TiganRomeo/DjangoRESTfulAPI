from django.urls import path
from app.views import UserAddAPIView, UserListAPIView, UserEdtAPIView, AuthAPIView

app_name = 'app'

urlpatterns = [
    path('api/1.0/auth/', AuthAPIView.as_view(), name='auth'),
    path('api/1.0/user/add/', UserAddAPIView.as_view(), name='user_add'),
    path('api/1.0/user/list/', UserListAPIView.as_view(), name='user_list'),
    path('api/1.0/user/edt/<int:id>/', UserEdtAPIView.as_view(), name='user_edt'),
]