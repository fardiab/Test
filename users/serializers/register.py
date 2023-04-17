from rest_framework import serializers

from users.models import User

class RegisterSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'password', 'username']