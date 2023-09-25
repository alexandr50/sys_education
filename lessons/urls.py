from django.urls import path

from lessons.views import LessonsListAPIView

urlpatterns = [
    path('', LessonsListAPIView.as_view(), name='lessons-for-product'),
    ]