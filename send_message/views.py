from django.shortcuts import render, HttpResponse
from .models import Dialog, Message
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def create_dialog(request, user_id):
    if request.user.is_authenticated:
        dialog_id = Dialog.objects.filter(
            user_1=request.user.id, user_2=user_id
        ) | Dialog.objects.filter(
            user_1=user_id, user_2=request.user.id
        )
        if not dialog_id:
            user_first = User.objects.get(id=user_id)
            user_second = User.objects.get(id=request.user.id)
            created = Dialog.objects.create(user_1=user_first, user_2=user_second)
        url = '/dialog/' + str(dialog_id.values()[0].get('id') if dialog_id else created.id) + '/'
        return HttpResponseRedirect(url)
    else:
        print('read again')
    return render(request, 'my_profile.html', locals())


@login_required
def dialog(request, dialog_id):
    if request.user.is_authenticated:
        messages = Message.objects.filter(dialog=dialog_id)
        print(messages)
        dialog = Dialog.objects.get(id=dialog_id)
        # print(messages)
        if request.method == 'POST':
            user_2 = dialog.user_2 if dialog.user_1 == request.user else dialog.user_1
            recipient = User.objects.get(id=user_2.id)
            print(recipient)
            sender = request.user
            message = request.POST['message']
            Message.objects.create(sender=sender, recipient=recipient, text_message=message, dialog=dialog)
            return render(request, 'room_page.html', locals())
    else:
        print('read again')
    return render(request, 'room_page.html', locals())


@login_required
def get_dialog(request):
    if request.user.is_authenticated:
        dialogs = dialog_id = Dialog.objects.filter(user_1=request.user.id) | Dialog.objects.filter(
            user_2=request.user.id)
    else:
        print('read again')
    return render(request, 'my_dialogs.html', locals())
