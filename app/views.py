from django.shortcuts import render
from django.http import HttpResponse 
from rest_framework.generics import CreateAPIView
from .models import User, Profile, MusicPost, Song, Comment, Like
from .serializers import UserSerializer, ProfileSerializer, MusicPostSerializer, SongSerializer,\
    CommentSerializer, LikeSerializer

# how to render the files in the web browser, directly passes Json data
# to send to React via Django routes

# views handle incoming requests, call the appropriate serializer 
# to process the data, & return a JSON response.

# handles user registration, creation of new user object
class RegisterView(CreateAPIView):
    serializer_class = UserSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
