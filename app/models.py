from django.db import models
import datetime 
from django.utils import timezone
from django.conf import settings 
from autoslug import AutoSlugField # makes meaningful URLS users/thao

# always have created at & updated at attributes (on every model)
# HOW ARE WE MAKING THE POST THAT GENERATES MUSIC STATS? DOES USER POST THAT?
# MUSIC STATS = POST? 
# MODEL FOR ACCOUNT & PROFILE?

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
# It let’s us define a meaningful name for the reverse relationship.
    

# ==== MusicStats model or Profile model?? === # 
class MusicPost(models.Model):   # post that shows music stats
    app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='music_posts')
    date = models.DateField(auto_now=True)
    # songs = models.CharField(max_length=255)   
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    # is_private = models.BooleanField     stretch goal
    

class MusicStat(models.Model):    # actual music stats
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    music_post = models.ForeignKey(MusicPost, on_delete=models.CASCADE)
    play_count = models.IntegerField(null=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    
    
# ===== COMMENT model  links comment w/ the post(music stat) & the user ===== #
class Comment(models.Model):
    music_post= models.ForeignKey(MusicPost, related_name='comment', on_delete=models.CASCADE)
    user = models.ForeignKey(AppUser, related_name='comment', on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    date_published = models.DateTimeField(auto_now_add=True)
    
    
# ====== LIKES model   stores like info   ====== #
class Like(models.Model):
    # user = represents user who liked post, deleting user deletes like
    user = models.ForeignKey(AppUser, related_name='like', on_delete=models.CASCADE)
    music_post = models.ForeignKey(MusicPost, related_name='like', on_delete=models.CASCADE)
    # post = the post on which the like is given, deleting post deletes all likes 

    # use same ForeignKey, to differentiate need
    
    
# ==== Profile model ===== # uses Django User model

class Profile(models.Model): 
    # 1:1 relationship w/ Django User model
    # if User deleted, profile destroyed too
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE) 
    # optional? for storing profile pic of user
    image = models.ImageField(default='default.png', upload_to='profile_pics') 
    # use AutoSlugField, set it to make a slug from user field
    slug = AutoSlugField(populate_from='user')
    # store small intro? blank=True means it can be left blank
    bio = models.CharField(max_length=255, blank=True)
    # many to many w/ Profile model, can be left blank 
    # every user can have multiple friends & can be frends w/ multiple ppl
    # friends = models.ManyToManyField("Profile", blank=True)x     # stretch
    
    
    
            
    # define get_absolute_url toget the abs URL for that profile
    def get_absolute_url(self):
        return "/users/{}".format(self.slug)      


    