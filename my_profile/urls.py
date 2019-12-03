from django.urls import path
from . import views

urlpatterns = [
	path('get_profile/', views.get_profile, name="get_profile"),
	path('logout_profile/', views.logout_profile, name="logout_profile"),
	path('show_my_profile/', views.show_my_profile, name="show_my_profile"),
	path('update_my_profile/', views.update_my_profile, name="update_my_profile"),
]