from django.urls import path
from . import views

urlpatterns = [
    path('api/1.0/auth/', views.auth, name='auth'),
    path('api/1.0/user/add/', views.add_user, name='add_user'),
    path('api/1.0/user/list/', views.list_users, name='list_users'),
    path('api/1.0/user/edt/<int:user_id>/', views.edit_user, name='edit_user'),
]