from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_password = request.POST['user_password']
        user = authenticate(request, username=user_name, password=user_password)
        if user is not None:
            print('ok')
            login(request, user)
            url = '/get_profile/'
            return HttpResponseRedirect(url)
        else:
            print('not')
    return render(request, 'home.html', locals())


def registration(request):
    user = 'name'
    if request.method == 'POST':
        username = request.POST['username']
        user_password = request.POST['password']
        user = User.objects.create_user(
            username, 'no_name@gmail.com', user_password)
        user.save()
        url = '/'
        return HttpResponseRedirect(url)

    return render(request, 'registration.html', locals())
