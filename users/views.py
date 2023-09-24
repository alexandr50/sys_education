from django.contrib.auth import login
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserCreateSerializer, UserLoginSerializer, UserSerializer
from .models import User


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        super().perform_create(serializer)
        serializer.save(user=self.request.user)

        # user = User.objects.create(**serializer.user)
        # login(self.request, user=serializer.user)

class LoginUserView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = UserLoginSerializer = self.get_serializer(data=request.data)
        data.is_valid(raise_exception=True)
        user = data.validated_data["user"]
        login(request, user=user)
        user_serializer = UserLoginSerializer(instance=user)
        return Response(user_serializer.data)

class ProfileUserView(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user



