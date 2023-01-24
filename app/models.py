from django.db import models
import datetime 
from django.utils import timezone


# class User(models.Model):
#     username = models.CharField(max_length=36, null=False)
#     first_name = models.CharField(max_length=36, null=False)
#     last_name = models.CharField(max=36, null=False)
    # password?? store encrypted in db, bcrypt library
    # also check password (manually)
    # or use 3rd party API OAuth, google, git (can be difficult)
    # can fake this info lol (form)
    
    
    # always have created at & updated at attributes (on every model)
    
# class Song(models.Model):
    