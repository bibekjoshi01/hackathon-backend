from elasticsearch_dsl import Q
from django_filters.filterset import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from src.product.models import Product, ProductCategory
from src.product.serializers import (
    ProductCategorySerializer,
    ProductCreateSerializer,
    ProductListSerializer,
    ProductRetrieveSerializer,
    ProductUpdateSerializer,
)


class FilterForProductViewSet(FilterSet):
    """Filters for Product ViewSet"""

    class Meta:
        model = Product
        fields = ["is_active", "category"]


class ProductViewSet(ModelViewSet):
    """Product ViewSet"""
                                                                                                                                                
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.filter(is_archived=False)
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = FilterForProductViewSet
    search_fields = ["name"]
    ordering = ["-created_at"]
    ordering_fields = ["id", "created_at"]
    http_method_names = ["options", "head", "get", "post", "patch"]

    def get_serializer_class(self):
        serializer_class = ProductListSerializer
        if self.request.method == "GET":
            if self.action == "list":
                serializer_class = ProductListSerializer
            else:
                serializer_class = ProductRetrieveSerializer
        if self.request.method == "POST":
            serializer_class = ProductCreateSerializer
        if self.request.method == "PATCH":
            serializer_class = ProductUpdateSerializer

        return serializer_class


class ProductCategoryListAPIView(ListAPIView):
    queryset = ProductCategory.objects.filter(is_active=True)
    serializer_class = ProductCategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering = ["name"]
    search_fields = ["name"]
    ordering_fields = ["name"]

