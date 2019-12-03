from django.shortcuts import render
from my_profile.models import Profile
from django.contrib.auth.decorators import login_required

from tidings.models import NewsModel


@login_required
def search_interlocutor(request):
    if request.user.is_authenticated:
        user_name = request.user
        group_users = Profile.objects.filter().exclude(user__username=user_name)
    else:
        print('read again')
    return render(request, 'search_people.html', locals())


@login_required
def profile_user(request, name_user):
    if request.user.is_authenticated:
        user_name = request.user
        user_detail = Profile.objects.get(user__username=name_user)
        news_model = NewsModel.objects.filter(user__username=user_name)
    else:
        print('read again')
    return render(request, 'user_inform.html', locals())
