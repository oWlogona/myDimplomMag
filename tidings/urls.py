from django.urls import path
from tidings.views import NewsList, NewsListView

urlpatterns = [
    path('my_news/', NewsList.as_view(), name="my_news"),
    path('add_news/', NewsListView.as_view(), name="add_news"),
]
