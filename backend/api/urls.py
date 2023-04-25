from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserAddView, UserListView, UserEditView, auth_view

urlpatterns = [
    path('auth/', auth_view),
    path('user/add/', UserAddView.as_view()),
    path('user/list/', UserListView.as_view()),
    path('user/edit/<int:pk>/', UserEditView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)