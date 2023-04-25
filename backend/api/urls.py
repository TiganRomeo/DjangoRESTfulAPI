from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import auth_view, UserAddView, UserListView, UserEditView

urlpatterns = [
    path('auth/', auth_view),
    path('user/add/', UserAddView.as_view()),
    path('user/list/', UserListView.as_view()),
    path('user/edit/<int:pk>/', UserEditView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)