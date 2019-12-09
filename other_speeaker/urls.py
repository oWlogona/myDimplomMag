from django.urls import path
from other_speeaker.views import SearchInterlocutor, ProfileUserView

urlpatterns = [
    path('search_interlocutor/', SearchInterlocutor.as_view(), name="search_interlocutor"),
    path('profile_user/<str:name_user>', ProfileUserView.as_view(), name="profile_user"),

]
