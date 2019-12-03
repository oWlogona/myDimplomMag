from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    user_age = models.IntegerField(blank=True, null=True, default=None)
    user_sex = models.CharField(max_length=16, blank=True, null=True, default=None)
    purpose_of_dating = models.CharField(max_length=32, blank=True, null=True, default=None)
    user_smook = models.CharField(max_length=32, blank=True, null=True, default=None)
    user_alcogol = models.CharField(max_length=32, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Профiль'
        verbose_name_plural = 'Профiль'