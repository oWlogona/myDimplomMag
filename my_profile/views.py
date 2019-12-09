from django.shortcuts import render
from django.views import View

from .models import Profile
from tidings.models import NewsModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'my_profile.html', locals())


@method_decorator(login_required, name='dispatch')
class ProfileDetailView(View):
    def get(self, request, *args, **kwargs):
        news_model = NewsModel.objects.filter(user__username=request.user.username)
        user = Profile.objects.get(user=request.user)
        return render(request, 'profile_user.html', locals())


@method_decorator(login_required, name='dispatch')
class ProfileEdit(View):
    def get(self, request, *args, **kwargs):
        user = Profile.objects.get_or_create(user=request.user)
        return render(request, 'update_profile.html', locals())

    def post(self, request, *args, **kwargs):
        print(request.POST)
        user = Profile.objects.filter(
            user=request.user).update(
            user_age=request.POST.get('user_age'),
            user_sex=request.POST.get('user_sex'),
            purpose_of_dating=request.POST.get('purpose_of_dating'),
            user_smook=request.POST.get('user_smook'),
            user_alcogol=request.POST.get('user_alcogol')
        )
        return render(request, 'update_profile.html', locals())
