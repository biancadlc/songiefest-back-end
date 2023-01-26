from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime 
from django.utils import timezone
from django.conf import settings 
from autoslug import AutoSlugField # makes meaningful URLS users/thao
# from django.utils.text import slugify

# always have created at & updated at attributes (on every model)

# changed name to User to avoid confusion w/ Django's default User model
# project's settings.py --> need to tell Django use custom model instead of default 

# null=False field not allowed to have NULL value in db, default  
# blank=False field can't be blank (validation for form)
# need to hash passwords, do not store in db 

class User(AbstractUser):  
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.CharField(unique=True, blank=False)
    password = models.CharField(max_length=30, blank=False)
    username = models.CharField(max_length=30, blank=False, unique=True)
    lastfm_username = models.CharField(max_length=30, blank=False, unique=True)
    lastfm_password = models.CharField(max_length=30, blank=False, unique=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    # auto_now_add=True sets current date/time when object is first created
    # auto_now=True sets field to the current date/time every time the object is saved
    

    # set it to show username as the Query object
    def __str__(self):
        return str(self.username)
    
    
# The related_name attribute in the ForeignKey fields is extremely useful. 
# defines a meaningful name for the reverse relationship.
# one instance of the model with the foreign key can be related to 
# multiple instances of the model it references
    

# ==== Music Post  ==== # 
# related_name= allows for retrieve all MusicPost records for a specific User
class MusicPost(models.Model):   # post that shows music stats
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='music_posts')
    date = models.DateField(auto_now=True)
    # songs = models.CharField(max_length=255)   
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    # unique constraint to the date field,can't have
    # two MusicPost records for same date
    # could use UniqueConstraint??
    
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['name', 'email'], name='unique_user')
    #     ]
        
    # user can't be registered with exact email & name 

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
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    
# ====== LIKES model   stores like info   ====== #
class Like(models.Model):
    # user = represents user who liked post, deleting user deletes like
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    music_post = models.ForeignKey(MusicPost, related_name='likes', on_delete=models.CASCADE)
    # post = the post on which the like is given, deleting post deletes all likes 
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # use same ForeignKey, to differentiate need
    
    
# ==== Profile model ===== # uses Django User model
# 1:1 relationship w/ User, each profile is unique to a user
# each user can have only one profile.
# if User deleted, profile destroyed too
# ForeignKey is used for one-to-many relationships
# need to use OntToOneField for one-to-one
# related_name singular for OneToOneField

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') 
    image = models.ImageField(default='default.png', upload_to='profile_pics', blank=True) 
    # store small bio? blank=True means it can be left blank
    bio = models.CharField(max_length=255, blank=True)
    # use AutoSlugField, set it to make a slug from username field
    slug = AutoSlugField(populate_from='app_user.username', unique=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    

    # returns URL for profle page of user by using `username` attribute 
    # of `app_user` field 
    def get_absolute_url(self):
        return "/users/{}".format(self.user.username)      

    # specifies that the URL should include "app_users" followed by 
    # value of the variable "slug" which is coming from Profile model
    # it is being populated w/ value of the app_user's username using the AutoSlugField.
    