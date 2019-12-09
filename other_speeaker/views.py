from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from my_profile.models import Profile
from django.contrib.auth.decorators import login_required

from tidings.models import NewsModel


@method_decorator(login_required, name='dispatch')
class SearchInterlocutor(View):
    def get(self, request, *args, **kwargs):
        group_users = Profile.objects.filter().exclude(user__username=request.user)
        return render(request, 'search_people.html', locals())


@method_decorator(login_required, name='dispatch')
class ProfileUserView(View):
    def get(self, request, name_user, *args, **kwargs):
        user_detail = Profile.objects.get(user__username=name_user)
        news_model = NewsModel.objects.filter(user__username=name_user)
        return render(request, 'user_inform.html', locals())
