from django_filters.filterset import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from src.product.models import Product
from src.product.serializers import (
    ProductCreateSerializer,
    ProductListSerializer,
    ProductRetrieveSerializer,
    ProductUpdateSerializer,
)


class FilterForProductViewSet(FilterSet):
    """Filters for Product ViewSet"""

    class Meta:
        model = Product
        fields = ["is_active"]


class ProductViewSet(ModelViewSet):
    """Product ViewSet"""

    # permission_classes = [ProductPermission]
    queryset = Product.objects.filter(is_archived=False)
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = FilterForProductViewSet
    search_fields = ["name"]
    ordering = ["-name"]
    rdering_fields = ["id", "created_at"]
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
