from django.urls import path

from .views import PublicProductListAPIView

urlpatterns = [path("products", PublicProductListAPIView.as_view())]
