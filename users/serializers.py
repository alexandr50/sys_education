from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password_repeat')


    def validate(self, attrs):
        password = attrs.get('password')
        password_repeat = attrs.pop('password_repeat')
        if password != password_repeat:
            raise ValueError('Passwords are not similar')
        return attrs


    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        self.user = user
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValueError('Username or Password invalid')
        return attrs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]
