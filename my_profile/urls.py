from django.urls import path
from my_profile.views import ProfileView, ProfileDetailView, ProfileEdit

urlpatterns = [
    path('get_profile/', ProfileView.as_view()),
    path('show_my_profile/', ProfileDetailView.as_view()),
    path('update_my_profile/', ProfileEdit.as_view()),
]
