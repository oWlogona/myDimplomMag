from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from .models import NewsModel


@method_decorator(login_required, name='dispatch')
class NewsList(View):
    def get(self, request, *args, **kwargs):
        news_model = NewsModel.objects.filter(user__username=request.user.username)
        print(news_model)
        return render(request, 'my_news.html', locals())


@method_decorator(login_required, name='dispatch')
class NewsListView(View):
    def get(self, request, *args, **kwargs):
        news_model = NewsModel.objects.filter(user__username=request.user.username).order_by('-created')
        return render(request, 'add_news.html', locals())

    def post(self, request, *args, **kwargs):
        text_news = request.POST.get('text_news')
        news_model = NewsModel.objects.filter(user__username=request.user.username).order_by('-created')
        user = NewsModel.objects.create(user=request.user, text_news=text_news)
        user.save()
        return render(request, 'add_news.html', locals())
