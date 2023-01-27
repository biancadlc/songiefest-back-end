from django.shortcuts import render
from django.http import HttpResponse 

# how to render the files in the web browser, directly passes Json data
# to send to React via Django routes

# views handle incoming requests, call the appropriate serializer 
# to process the data, & return a JSON response.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
