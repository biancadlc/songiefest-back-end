from django.contrib import admin
from .models import User, Profile, MusicPost, Song, Comment, Like

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(MusicPost)
admin.site.register(Song)
admin.site.register(Comment)
admin.site.register(Like)


# test to see that CRUD operations work on User model
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'username', 'email', 'password', 'lastfm_username', \
#         'lastfm_password', 'date_published', 'date_modified')

