from django.urls import path
from app.views import AuthView, UserAddView, UserListView, UserEditView

urlpatterns = [
    path('api/1.0/auth/', AuthView.as_view(), name='auth'),
    path('api/1.0/user/add/', UserAddView.as_view(), name='user-add'),
    path('api/1.0/user/list/', UserListView.as_view(), name='user-list'),
    path('api/1.0/user/edt/<int:pk>/', UserEditView.as_view(), name='user-edt'),
]