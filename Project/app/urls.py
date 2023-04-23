from django.urls import path
from .views import AuthAPI, UserAPI

urlpatterns = [
    path('auth/', AuthAPI.as_view()),
    path('user/add/', UserAPI.as_view({'post': 'create'})),
    path('user/list/', UserAPI.as_view({'get': 'list'})),
    path('user/edit/<int:pk>/', UserAPI.as_view({'put': 'update'})),
]