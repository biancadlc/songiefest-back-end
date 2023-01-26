from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, MusicStat, Comment, Like, MusicPost

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(MusicPost)
admin.site.register(MusicStat)
admin.site.register(Comment)
admin.site.register(Like)
