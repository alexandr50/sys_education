from django.contrib import admin

from lessons.models import Lesson, UserLesson

admin.site.register(Lesson)
admin.site.register(UserLesson)
