from django.urls import path
from .views import AuthView

urlpatterns = [
    path('', AuthView.as_view()), # localhost:8000/api/1.0/
]
