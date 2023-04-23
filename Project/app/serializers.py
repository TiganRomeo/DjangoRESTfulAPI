from rest_framework import serializers
from .models import User

# -----------------------------------------------------

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[validate_not_empty])

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'age')
# - Used for converting User objects into JSON format -