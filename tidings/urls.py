from django.urls import path
from . import views

urlpatterns = [
	path('my_news/', views.my_news, name="my_news"),
	path('add_news/', views.add_news, name="add_news"),
]