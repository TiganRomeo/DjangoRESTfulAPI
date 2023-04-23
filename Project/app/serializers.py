from django.contrib.auth.models import User
from rest_framework import serializers


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = User.objects.filter(username=data['username']).first()

        if user and user.check_password(data['password']):
            return data
        else:
            raise serializers.ValidationError('Incorrect credentials')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']
        read_only_fields = ['id']