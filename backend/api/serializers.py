from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password', 'is_active', 'is_staff', 'is_superuser')

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'],
                                        password=validated_data['password'],
                                        name=validated_data['name'],
                                        is_active=validated_data.get('is_active', True),
                                        is_staff=validated_data.get('is_staff', False),
                                        is_superuser=validated_data.get('is_superuser', False))
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance