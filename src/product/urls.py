from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import ProductDescriptionAPIView, ProductViewSet, ProductCategoryListAPIView

router = DefaultRouter(trailing_slash=False)

router.register("products", ProductViewSet, basename="products")

urlpatterns = [
    *router.urls,
    path("categories", ProductCategoryListAPIView.as_view()),
    path(
        "generate-description",
        ProductDescriptionAPIView.as_view(),
        name="generate-description",
    ),
]
