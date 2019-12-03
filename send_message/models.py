from django.db import models
from django.contrib.auth.models import User


class Dialog(models.Model):
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_1')
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_2')

    def __str__(self):
        return "{} - {}".format(self.user_1, self.user_2)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='recipient', on_delete=models.CASCADE)
    text_message = models.CharField(max_length=255, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    dialog = models.ForeignKey(Dialog, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.sender.username
