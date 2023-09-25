
from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer, StatisticSerializer, LessonSerializer


class ProductListAPIView(generics.ListAPIView):

    serializer_class = LessonSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = Product.objects.filter(owner__id=self.request.user.id)
        return queryset

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class StatisticView(generics.ListAPIView):
    serializer_class = StatisticSerializer
    queryset = Product.objects.all()

