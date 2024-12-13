from django.urls import path

from .views import PublicCategoryListAPIView, PublicProductListAPIView

urlpatterns = [
    path("products", PublicProductListAPIView.as_view()),
    path("categories", PublicCategoryListAPIView.as_view()),
]
