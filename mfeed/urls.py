from django.urls import path,include
from .views import AuthUserRegistrationView,LoginAPIView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/',AuthUserRegistrationView.as_view()),
    path('login/',LoginAPIView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_create'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
