from django.urls import path

from .views import (
    PublicCategoryListAPIView,
    PublicProductListAPIView,
    PublicProductRetrieveAPIView,
)

urlpatterns = [
    path("products", PublicProductListAPIView.as_view()),
    path(
        "products/<int:id>",
        PublicProductRetrieveAPIView.as_view(),
        name="product-detail",
    ),
    path("categories", PublicCategoryListAPIView.as_view()),
]
