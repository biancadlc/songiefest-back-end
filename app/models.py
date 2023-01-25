from django.db import models
import datetime 
from django.utils import timezone
from django.conf import settings 
from autoslug import AutoSlugField # makes meaningful URLS users/thao


# 2 models, 1 = user's profile, 2 = friend requests
# always have created at & updated at attributes (on every model)
# HOW ARE WE MAKING THE POST THAT GENERATES MUSIC STATS? DOES USER POST THAT?
# MUSIC STATS = POST? 
# MODEL FOR ACCOUNT & PROFILE?

class User(models.Model):  
    username = models.CharField(max_length=36, null=False)
    first_name = models.CharField(max_length=36, null=False)
    last_name = models.CharField(max_length=36, null=False)
    email = models.CharField(max_length=36, null=False)
    password = models.CharField(max_length=16, null=False)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    
    # lastfm username & password? (CharField)
    # spotify_access_token & spotify_refresh_token? (CharField)
    # friends   # stretch goal
    
    # decides how Django will show our model in admin panel
    # set it to show username as the Query object
    def __str__(self):
        return str(self.username)
    
    
    

# ==== MusicStats model or Profile model?? === # 
class MusicPost(models.Model):   # post that shows music stats
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField
    songs = models.CharField(max_length=255)   
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    # is_private = models.BooleanField     stretch goal
    
    
class MusicStat(models.Model):    # actual music stats
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    music_post = models.ForeignKey(MusicPost, on_delete=models.CASCADE)
    play_count = models.IntegerField
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    
    
# ===== COMMENT model  links comment w/ the post(music stat) & the user ===== #
class Comment(models.Model):
    music_post= models.ForeignKey(MusicPost, related_name='comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    date_published = models.DateTimeField(auto_now_add=True)
    
    
# ====== LIKES model   stores like info   ====== #
class Like(models.Model):
    # user = represents user who liked post, deleting user deletes like
    user = models.ForeignKey(User, related_name='like', on_delete=models.CASCADE)
    music_post = models.ForeignKey(MusicPost, related_name='like', on_delete=models.CASCADE)
    # post = the post on which the like is given, deleting post deletes all likes 

    # use same ForeignKey, to differentiate need
    
    
# ==== Profile model ===== # uses Django User model

class Profile(models.Model): 
    # 1:1 relationship w/ Django User model
    # if User deleted, profile destroyed too
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
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


    