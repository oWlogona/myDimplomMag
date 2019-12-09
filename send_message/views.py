from django.shortcuts import render, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View

from .models import Dialog, Message
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class DialogCreate(View):
    def get(self, request, user_id, *args, **kwargs):
        dialog_id = Dialog.objects.filter(
            user_1=request.user.id, user_2=user_id) | Dialog.objects.filter(user_1=user_id, user_2=request.user.id)
        if not dialog_id:
            user_first = User.objects.get(id=user_id)
            user_second = User.objects.get(id=request.user.id)
            created = Dialog.objects.create(user_1=user_first, user_2=user_second)
        url = '/dialog/' + str(dialog_id.values()[0].get('id') if dialog_id else created.id) + '/'
        return HttpResponseRedirect(url)


@method_decorator(login_required, name='dispatch')
class DialogView(View):
    def get(self, request, dialog_id, *args, **kwargs):
        messages = Message.objects.filter(dialog=dialog_id)
        dialog = Dialog.objects.get(id=dialog_id)
        return render(request, 'room_page.html', locals())

    def post(self, request, dialog_id, *args, **kwargs):
        messages = Message.objects.filter(dialog=dialog_id)
        dialog = Dialog.objects.get(id=dialog_id)
        user_2 = dialog.user_2 if dialog.user_1 == request.user else dialog.user_1
        recipient = User.objects.get(id=user_2.id)
        sender = request.user
        message = request.POST['message']
        Message.objects.create(sender=sender, recipient=recipient, text_message=message, dialog=dialog)
        return render(request, 'room_page.html', locals())


@method_decorator(login_required, name='dispatch')
class DialogListView(View):
    def get(self, request, *args, **kwargs):
        dialogs = dialog_id = Dialog.objects.filter(user_1=request.user.id) | Dialog.objects.filter(
            user_2=request.user.id)
        return render(request, 'my_dialogs.html', locals())
