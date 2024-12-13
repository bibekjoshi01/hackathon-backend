from django.urls import path
from .views import (
    BusinessCategoryListAPIView,
    BusinessInfoCreateAPIView,
    BusinessInfoListAPIView,
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
    path(
        "business-info/<int:farmer_id>",
        BusinessInfoListAPIView.as_view(),
        name="business-info-detail",
    ),
    path("categories", BusinessCategoryListAPIView.as_view()),
]
