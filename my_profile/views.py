from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from .models import Profile
from tidings.models import NewsModel
from django.contrib.auth.decorators import login_required


@login_required
def get_profile(request):
    if request.user.is_authenticated:
        user_name = request.user.username
    else:
        print('read again')
    return render(request, 'my_profile.html', locals())


@login_required
def show_my_profile(request):
    if request.user.is_authenticated:
        user_name = request.user.username
        user_check = Profile.objects.filter(user__username=user_name)
        print(user_check)
        news_model = NewsModel.objects.filter(user__username=user_name)
        if user_check:
            user = Profile.objects.get(user=request.user)
        else:
            print('not')
    return render(request, 'profile_user.html', locals())


@login_required
def update_my_profile(request):
    if request.user.is_authenticated:
        user_name = request.user.username
        print('ok')
        user_check = Profile.objects.filter(user__username=user_name)
        if not user_check:
            user = Profile.objects.create(user=request.user)

        if request.method == 'POST':
            user_age = request.POST.get('user_age')
            user_sex = request.POST.get('user_sex')
            purpose_of_dating = request.POST.get('purpose_of_dating')
            user_smook = request.POST.get('user_smook')
            user_alcogol = request.POST.get('user_alcogol')
            user = Profile.objects.filter(user=request.user).update(user_age=user_age,
                                                                    user_sex=user_sex,
                                                                    purpose_of_dating=purpose_of_dating,
                                                                    user_smook=user_smook, user_alcogol=user_alcogol)
    else:
        print('read again')
    return render(request, 'update_profile.html', locals())


def logout_profile(request):
    logout(request)
    url = '/'
    return HttpResponseRedirect(url)
