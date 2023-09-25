from rest_framework import serializers

from lessons.models import Lesson
from lessons.serializers import LessonSerializer
from products.models import Product


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
