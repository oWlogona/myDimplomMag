from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class UserLogin(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            url = '/get_profile/'
            return HttpResponseRedirect(url)
        return render(request, self.template_name, locals())


class UserRegistration(View):
    template_name = 'registration.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        request_data = request.POST
        if request_data.get('username') and request_data.get('password'):
            user = User.objects.create_user(
                username=request_data.get('username'),
                email='{}@gmail.com'.format(request_data.get('username')),
                password=request_data.get('password')
            )
            user.save()
            url = '/'
            return HttpResponseRedirect(url)
        return render(request_data, self.template_name, locals())


@method_decorator(login_required, name='dispatch')
class UserLogOut(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        url = '/'
        return HttpResponseRedirect(url)
