from django.urls import path
from app import views

urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('user/add/', views.add_user, name='user-add'),
    path('user/list/', views.list_users, name='user-list'),
    path('user/edt/<int:pk>/', views.edit_user, name='user-edt'),
]