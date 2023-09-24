from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import CreateUserView, LoginUserView, ProfileUserView

urlpatterns = [
    path('register', CreateUserView.as_view(), name='register'),
    path('login', LoginUserView.as_view(), name='login'),
    path('profile', ProfileUserView.as_view(), name='profile'),
]
