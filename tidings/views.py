from django.shortcuts import render
from .models import NewsModel


def my_news(request):
    if request.user.is_authenticated:
        user_name = request.user.username
        print('ok')
        news_model = NewsModel.objects.filter(user__username=user_name)

    return render(request, 'my_news.html', locals())


def add_news(request):
    if request.user.is_authenticated:
        user_name = request.user.username
        news_model = NewsModel.objects.filter(user__username=user_name).order_by('-created')

        if request.method == 'POST':
            text_news = request.POST.get('text_news')
            user = NewsModel.objects.create(user=request.user, text_news=text_news)
            user.save()

    return render(request, 'add_news.html', locals())
