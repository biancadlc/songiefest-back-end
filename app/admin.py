from django.contrib import admin
from .models import AppUser, Profile, MusicStat, Comment, Like, MusicPost

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Profile)
admin.site.register(MusicPost)
admin.site.register(MusicStat)
admin.site.register(Comment)
admin.site.register(Like)
