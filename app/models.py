from django.db import models
import datetime 
from django.utils import timezone
from django.conf import settings 
from autoslug import AutoSlugField # makes meaningful URLS users/thao

# always have created at & updated at attributes (on every model)

# changed name to AppUser to avoid confusion w/ Django's default User model
# project's settings.py --> need to tell Django use custom model instead of default 

# null=False field not allowed to have NULL value in db, default  
# blank=False field can't be blank (validation for form)
# need to hash passwords, do not store in db 

class AppUser(models.Model):  
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)
    username = models.CharField(max_length=30, null=False, blank=False, unique=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    lastfm_username = models.CharField(max_length=30, null=False, blank=False, unique=True)
    lastfm_password = models.CharField(max_length=30, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # auto_now_add=True sets current date/time when object is first created
    # auto_now=True sets field to the current date/time every time the object is saved
    

    # set it to show username as the Query object
    def __str__(self):
        return str(self.username)
    
    
# The related_name attribute in the ForeignKey fields is extremely useful. 
# defines a meaningful name for the reverse relationship.
# one instance of the model with the foreign key can be related to 
# multiple instances of the model it references
    

# ==== MusicStats model or Profile model?? === # 
class MusicPost(models.Model):   # post that shows music stats
    app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='music_posts')
    date = models.DateField(auto_now=True)
    # songs = models.CharField(max_length=255)   
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    # is_private = models.BooleanField     stretch goal
    

class MusicStat(models.Model):    # actual music stats
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    album = models.CharField(max_length=30)
    music_post = models.ForeignKey(MusicPost, on_delete=models.CASCADE, related_name='music_stats')
    play_count = models.IntegerField(null=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    
    # playcount null allow bc this might not be known when model is first created
    
    
# ===== COMMENT model  links comment w/ the post(music stat) & the user ===== #
class Comment(models.Model):
    music_post= models.ForeignKey(MusicPost, related_name='comments', on_delete=models.CASCADE)
    app_user = models.ForeignKey(AppUser, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    date_published = models.DateTimeField(auto_now_add=True)
    
    
# ====== LIKES model   stores like info   ====== #
class Like(models.Model):
    # user = represents user who liked post, deleting user deletes like
    user = models.ForeignKey(AppUser, related_name='likes', on_delete=models.CASCADE)
    music_post = models.ForeignKey(MusicPost, related_name='likes', on_delete=models.CASCADE)
    # post = the post on which the like is given, deleting post deletes all likes 

    # use same ForeignKey, to differentiate need
    
    
# ==== Profile model ===== # uses Django User model
# 1:1 relationship w/ AppUser, each profile is unique to a user
# each user can have only one profile.
# if User deleted, profile destroyed too
# ForeignKey is used for one-to-many relationships
# need to use OntToOneField for one-to-one
# related_name singular for OneToOneField

class Profile(models.Model): 
    app_user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='profile') 
    image = models.ImageField(default='default.png', upload_to='profile_pics', blank=True) 
    # use AutoSlugField, set it to make a slug from username field
    slug = AutoSlugField(populate_from='app_user.username', unique=True)
    # store small bio? blank=True means it can be left blank
    bio = models.CharField(max_length=255, blank=True)    
    

    # returns URL for profle page of user by using `username` attribute 
    # of `app_user` field 
    def get_absolute_url(self):
        return "/app_users/{}".format(self.app_user.username)      

    # specifies that the URL should include "app_users" followed by 
    # value of the variable "slug" which is coming from Profile model
    # it is being populated w/ value of the app_user's username using the AutoSlugField.
    