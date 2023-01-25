from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
import datetime 
from django.utils import timezone
from django.db.models.signals import post_save
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
    last_name = models.CharField(max=36, null=False)
    email = models.CharField(max=36, null=False)
    password = models.CharField(max_length=16, null=False)
    # lastfm username & password? (CharField)
    # spotify_access_token & spotify_refresh_token? (CharField)
    # friends?? 

# ==== MusicStats model or Profile model?? === #
class MusicStat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    play_count = models.IntegerField
    month = models.DateField
    is_private = models.BooleanField

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
    friends = models.ManyToManyField("Profile", blank=True)
    
    
    # decides how Django will show our model in admin panel
    # set it to show username as the Query object
    def __str__(self):
        return str(self.user.username)
            
    # define get_absolute_url toget the abs URL for that profile
    def get_absolute_url(self):
        return "/users/{}".format(self.slug)      

    
# def post_save_user_model_reciever(sender, instance, created, *args, **kwargs):
#     if created:
#         try:
#             Profile.objects.create(user=instance)
#         except:
#             pass
        
# post_save.connect(post_save_user_model_reciever, sender=settings.AUTH_USER_MODEL)
    
# ==== Possibly 2nd App for FEED? with the below models? ====#

# ==== POST model ==== # for post user posts on website 
# class Post(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     pic = models.ImageField(upload_to='path/to/img')
#     date_posted = models.DateTimeField(default=timezone.now)
#     user_name = models.ForeignKey(User, on_delete=models.CASCADE)
#     tags = models.CharField(max_length=100, blank=True)


    # def __str__(self):
    #     return self.description
    
    # def get_absolute_url(self):
    #     return reverse("post-detail", kwargs={"pk": self.pk})
    
# ===== COMMENT model  links comment w/ the post(music stat) & the user ===== #
class Comment(models.Model):
    music_stat = models.ForeignKey(MusicStat, related_name='comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    comment_date = models.DateTimeField(default=timezone.now)
    
    
# ====== LIKES model   stores like info   ====== #
class Like(models.Model):
    # user = represents user who liked post, deleting user deletes like
    user = models.ForeignKey(User, related_name='like', on_delete=models.CASCADE)
    music_stat = models.ForeignKey(MusicStat, related_name='like', on_delete=models.CASCADE)
    # post = the post on which the like is given, deleting post deletes all likes 

    # use same ForeignKey, to differentiate need
    # to use related_name field 
    

        
# ===== FRIEND REQUEST MODEL  ==== #    STRETCH FEATURE 
# class FriendRequest(models.Model): 
#     # denotes the user to whom fr will be sent
#     to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)  
#     # denotes the user who is sending fr
#     from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
#     # optional, stores time when fr sent
#     timestamp = models.DateTimeField(auto_now_add=True)   

    
#     def __str__(self):
#         return "From {}, to {}".format(self.from_user.username, self.to_user.username)
# both to_user and from_user use same ForeignKey, to differentiate need
# to use related_name field 




    


    
    
    
    
    