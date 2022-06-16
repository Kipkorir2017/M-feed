from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView
from . import views
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('profile/',views.ProfileList.as_view()),
    path('survey/',views.SurveyList.as_view()),
    path('reports/',views.ReportsList.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    
]