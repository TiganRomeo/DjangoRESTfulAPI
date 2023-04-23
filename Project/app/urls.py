from django.urls import path
from app.views import auth, add_user, list_users, edit_user

urlpatterns = [
    path('auth/', auth.as_view(), name='auth'),
    path('user/add/', add_user.as_view(), name='user-add'),
    path('user/list/', list_users.as_view(), name='user-list'),
    path('user/edt/<int:pk>/', edit_user.as_view(), name='user-edt'),
]