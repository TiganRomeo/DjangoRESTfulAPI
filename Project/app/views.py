from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, validate_not_empty


class UserCreateAPIView(generics.CreateAPIView):
    """
    API view to create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """
        Override perform_create method to hash the password before saving it to the database.
        """
        password = serializer.validated_data.get('password', None)
        if password is not None:
            serializer.validated_data['password'] = make_password(password)
        serializer.save()

    def post(self, request, *args, **kwargs):
        """
        Override post method to validate the data before creating the user.
        """
        data = request.data.copy()
        validate_not_empty(data.get('username', ''))
        validate_not_empty(data.get('email', ''))
        validate_not_empty(data.get('password', ''))
        return super().post(request, *args, **kwargs)


class UserListAPIView(generics.ListAPIView):
    """
    API view to list all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    API view to update a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        """
        Override perform_update method to hash the password before saving it to the database.
        """
        password = serializer.validated_data.get('password', None)
        if password is not None:
            serializer.validated_data['password'] = make_password(password)
        serializer.save()