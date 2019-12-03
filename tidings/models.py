from django.db import models
from django.contrib.auth.models import User


class NewsModel(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    text_news = models.TextField(max_length=242)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
