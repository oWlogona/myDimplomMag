from django.urls import path
from . import views

urlpatterns = [
    path('create_dialog/<int:user_id>/', views.create_dialog, name='create_dialog'),
    path('dialog/<int:dialog_id>/', views.dialog, name='dialog'),
    path('my_dialog/', views.get_dialog, name='get_dialog'),
]
