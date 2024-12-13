from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PublicUserSignInAPIView,
    PublicUserSignUpAPIView,
    PublicUserSocialAuthAPIView,
    PublicUserLogoutAPIView
)

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path(
        "users/social/auth",
        PublicUserSocialAuthAPIView.as_view(),
        name="public_user_social_auth",
    ),
    path(
        "users/signin",
        PublicUserSignInAPIView.as_view(),
        name="public_user_signin",
    ),
    path(
        "users/signup",
        PublicUserSignUpAPIView.as_view(),
        name="public_user_signup",
    ),
    path("users/logout", PublicUserLogoutAPIView.as_view(), name="public_user_logout"),
    path("", include(router.urls)),
]
