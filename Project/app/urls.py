from django.urls import path
from .views import auth, add_user, list_users, edit_user

urlpatterns = [
    path('auth/', auth),
    path('user/add/', add_user),
    path('user/list/', list_users),
    path('user/edt/<int:pk>/', edit_user),
]