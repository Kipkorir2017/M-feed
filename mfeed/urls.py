from django.urls import path,include
from .views import AuthUserRegistrationView,LoginAPIView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, LoginView, UserView, LogoutView
from . import views
from rest_framework import routers
from .views import ChangePasswordView

router=routers.DefaultRouter()
router.register('profile',views.ProfileList )
router.register('survey',views.SurveyList )
router.register('report',views.ReportList )

urlpatterns = [
    path('register/',AuthUserRegistrationView.as_view()),
    path('login/',LoginAPIView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_create'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/',include(router.urls)),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
    path('download/',views.download,name='downloads'),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('password-reset-complete', views.SetNewPasswordAPIView.as_view(),name='password-reset-complete'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


