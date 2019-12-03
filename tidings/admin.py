from django.contrib import admin
from .models import NewsModel

class NewsModelAdmin(admin.ModelAdmin):
	list_display = [field.name for field in NewsModel._meta.fields]


admin.site.register(NewsModel, NewsModelAdmin)