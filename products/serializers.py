from datetime import timedelta

from rest_framework import serializers

from lessons.models import Lesson, UserLessonViewed
from lessons.serializers import LessonSerializer
from products.models import Product
from users.models import User


class ProductSerializer(serializers.ModelSerializer):
    product_lessons = LessonSerializer(source='lesson', many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_product_lessons(self, instance):
        request = self._context["request"]
        return Lesson.objects.filter(product=instance.id).exists()


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class StatisticSerializer(serializers.ModelSerializer):
    watched_owners = serializers.SerializerMethodField()
    total_duration = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()
    percents = serializers.SerializerMethodField()



    def get_watched_owners(self, instance):
        lessons = Lesson.objects.filter(product=instance)
        count = 0
        for les in lessons:
            query_viewed = UserLessonViewed.objects.filter(lesson__id=les.id)
            if query_viewed:
                for time in query_viewed:
                    if time.status =='Посмотренно':
                        count += 1

        return count

    def get_total_duration(self, instance):
        lessons = Lesson.objects.filter(product=instance)
        count = timedelta(0)
        for les in lessons:
            query_viewed = UserLessonViewed.objects.filter(lesson__id=les.id)
            if query_viewed:
                for time in query_viewed:
                    if time.watched_time:
                        count += time.watched_time

        return count

    def get_students(self, instance):
        self.product_students_count = len(instance.students.select_related())
        return self.product_students_count

    def get_percents(self, instance):
        return self.product_students_count / len(User.objects.all())


    class Meta:
        model = Product
        fields = ('watched_owners', 'total_duration', 'students', 'percents')



