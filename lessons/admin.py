from django.contrib import admin

from lessons.models import Lesson, UserLessonViewed

admin.site.register(Lesson)
admin.site.register(UserLessonViewed)
