from django.urls import path
from send_message.views import DialogCreate, DialogView, DialogListView

urlpatterns = [
    path('create_dialog/<int:user_id>/', DialogCreate.as_view()),
    path('dialog/<int:dialog_id>/', DialogView.as_view(), name='dialog'),
    path('my_dialog/', DialogListView.as_view(), name='get_dialog'),
]
