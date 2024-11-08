from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from rest_framework.authtoken import views as token_views
from .views import Sign, Verify, Welcome


urlpatterns = [
    path('auth/sign', Sign.as_view(), name="sign"),
    path('auth/verify', Verify.as_view(), name="verify"),
    path('welcome', Welcome.as_view(), name="welcome"),
    # path('auth/login', token_views.obtain_auth_token, name="login_token"),
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
