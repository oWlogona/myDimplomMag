from django.urls import path
from . import views

urlpatterns = [
	path('search_interlocutor/', views.search_interlocutor, name="search_interlocutor"),
	path('profile_user/<str:name_user>', views.profile_user, name="profile_user"),

]