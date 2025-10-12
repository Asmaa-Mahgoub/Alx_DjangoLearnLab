
from .models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'date_of_birth', 'location']
        read_only_fields = ['followers']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)  # Create a token for the new user
        return user
    

        

