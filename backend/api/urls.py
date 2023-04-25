from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('user/add/', views.user_add, name='user_add'),
    path('user/list/', views.user_list, name='user_list'),
    path('user/edit/<int:pk>/', views.user_edit, name='user_edit'),
]