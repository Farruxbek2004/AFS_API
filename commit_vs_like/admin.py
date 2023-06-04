from django.contrib import admin
from .models import LikeDislike, Comment

# Register your models here.

admin.site.register(LikeDislike)
admin.site.register(Comment)
