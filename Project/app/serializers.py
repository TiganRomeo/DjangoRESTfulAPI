from rest_framework import serializers
from .models import User

# -----------------------------------------------------

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'created_at', 'updated_at']
    
# - Used for converting User objects into JSON format -