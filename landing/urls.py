from django.urls import path
from landing.views import UserLogin, UserRegistration, UserLogOut

urlpatterns = [
    path('', UserLogin.as_view()),
    path('registration/', UserRegistration.as_view()),
    path('logout_profile/', UserLogOut.as_view()),
]
