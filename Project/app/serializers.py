from rest_framework import serializers
from django.contrib.auth.models import User


def validate_not_empty(value):
    """
    Custom validator to ensure that a string field is not empty.
    """
    if not value.strip():
        raise serializers.ValidationError("This field cannot be empty.")


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for User model.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Override create method to hash the password before saving it to the database.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """
        Override update method to hash the password before saving it to the database.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password', None)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance