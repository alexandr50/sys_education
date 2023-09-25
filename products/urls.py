from django.urls import path

from products.views import ProductListAPIView, ProductCreateView, StatisticView

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('detail', ProductListAPIView.as_view(), name='product-detail'),
    path('create', ProductCreateView.as_view(), name='product-create'),
    path('statistic', StatisticView.as_view(), name='statistic'),

    ]