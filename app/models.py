from django.db import models
import datetime 
from django.utils import timezone
from django.conf import settings 
from autoslug import AutoSlugField # makes meaningful URLS users/thao



# always have created at & updated at attributes (on every model)

class User(models.Model):  
    first_name = models.CharField(max_length=36, blank=False)
    last_name = models.CharField(max_length=36, null=False)
    username = models.CharField(max_length=36, blank=False, unique=True)
    email = models.CharField(max_length=36, blank=False, unique=True)
    password = models.CharField(max_length=16, blank=False)
    lastfm_username = models.CharField(max_length=36, blank=False, unique=True)
    lastfm_password = models.CharField(max_length=36, blank=False, unique=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
                                

    # set it to show username as the Query object
    def __str__(self):
        return str(self.username)
    
# The related_name attribute in the ForeignKey fields is extremely useful
# defines a meaningful name for the reverse relationship.
# one instance of the model with the foreign key can be related to 
# multiple instances of the model it references
    

# ==== Music Post ==== #
# related_name= allows for retrieve all MusicPost records for a specific User

class MusicPost(models.Model):   # post that shows music stats
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='music_posts')
    date = models.DateField(auto_now=True)
    # songs = models.CharField(max_length=255)   
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # add unique constraint to the date field, can't have 2 musicpost records
    # for the same date? UniqueConstraint??
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['name', 'email'], name='unique_user')
    #     ]
        
    # user can't be registered with exact email & name 
    
    
class Song(models.Model):    # actual music stats
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    music_post = models.ForeignKey(MusicPost, on_delete=models.CASCADE, related_name='songs')
    play_count = models.IntegerField(null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    
    # playcount null=True bc this might not be known when model is first created
    
    
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
    
    
# ==== Profile model ===== # 
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
    slug = AutoSlugField(populate_from='user.username', unique=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    

    # returns URL for profle page of user by using `username` attribute 
    # of `app_user` field 
    def get_absolute_url(self):
        return "/users/{}".format(self.user.username)      

    # specifies that the URL should include "users" followed by 
    # value of the variable "slug" which is coming from Profile model
    # it is being populated w/ value of the user's username using the AutoSlugField.




