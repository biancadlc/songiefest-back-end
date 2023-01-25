from django.contrib import admin
from .models import Profile, MusicStat, Comment, Like

# Register your models here.
admin.site.register(Profile)
#admin.site.register(FriendRequest)

admin.site.register(MusicStat)
admin.site.register(Comment)
admin.site.register(Like)