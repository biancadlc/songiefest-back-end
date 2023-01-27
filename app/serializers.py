from rest_framework import serializers
from .models import User, Profile, MusicPost, Song, Comment, Like


# specifies the models to work w/ & the fields to be converted to JSON
# converts objects into data types understandable by React
# include specific fields in the serialization or list all '__all__'

# id field automatically added by Django as primary key for each model
# when its created in db, should include in serialized output bc required field in db
# maybe useful to include in response from our API??

# fields included in serializer --> what data is returned in API response
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'date_published')
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'image', 'bio', 'slug')

        
class MusicPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicPost
        fields = ('id', 'user', 'date', 'date_published')
        

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'album', 'play_count')
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'text', 'date_published')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'date_published')


        