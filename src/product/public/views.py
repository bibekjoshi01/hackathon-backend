from rest_framework.generics import ListAPIView
from django_filters.filterset import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from src.product.models import Product, ProductCategory
from .serializers import PublicProductListSerializer, ProductCategorySerializer


class PublicCategoryListAPIView(ListAPIView):
    queryset = ProductCategory.objects.filter(is_active=True)
    serializer_class = ProductCategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering = ["name"]
    search_fields = ["name"]
    ordering_fields = ["name"]


class PublicProductListAPIView(ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = PublicProductListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["price", "category"]
    search_fields = ["name"]
    ordering = ["-name", "price"]
    ordering_fields = ["id", "price"]
