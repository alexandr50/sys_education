from datetime import timedelta

from rest_framework import serializers

from lessons.models import Lesson, UserLessonViewed
from products.models import Product
from users.models import User


class LessonSerializer(serializers.ModelSerializer):
    """serialiser for product with details."""
    view_details = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ('name', 'view_details')

    def get_view_details(self, instance) -> dict:
        request = self.context.get("request")
        product = UserLessonViewed.objects.filter(owner_id=request.user.id, lesson_id=instance.id)
        if product:
            product = product.first()
            return {
                'viewed_length': product.watched_time,
                'is_viewed': product.status,
                'last_watched': product.last_watched,
            }


class ProductSerializer(serializers.ModelSerializer):
    """serializer for all lessons in products"""
    product_lessons = LessonSerializer(source='lesson', many=True, read_only=True)

    def get_product_lessons(self, instance):
        request = self._context["request"]
        return Lesson.objects.filter(product=instance.id).exists()

    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class StatisticSerializer(serializers.ModelSerializer):
    """serializer for statistic"""

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
                    if time.status == 'Посмотренно':
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
