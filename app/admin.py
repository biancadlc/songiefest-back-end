from django.contrib import admin
from .models import User, Profile, MusicPost, Song, Comment, Like

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(MusicPost)
admin.site.register(Song)
admin.site.register(Comment)
admin.site.register(Like)