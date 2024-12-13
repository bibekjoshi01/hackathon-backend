from django.urls import path
from .views import (
    BusinessCategoryListAPIView,
    BusinessInfoCreateAPIView,
    BusinessInfoUpdateAPIView,
)

urlpatterns = [
    path(
        "business-info/create",
        BusinessInfoCreateAPIView.as_view(),
        name="business-info-create",
    ),
    path(
        "business-info/update",
        BusinessInfoUpdateAPIView.as_view(),
        name="business-info-update",
    ),
    path("categories", BusinessCategoryListAPIView.as_view()),
]
