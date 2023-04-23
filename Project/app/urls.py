from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import AuthAPI, UserList, UserDetail


urlpatterns = [
    path('auth/', AuthAPI.as_view()),
    path('user/add/', UserList.as_view()),
    path('user/list/', UserList.as_view()),
    path('user/edit/<int:pk>/', UserDetail.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # For obtaining token through browsable API
]