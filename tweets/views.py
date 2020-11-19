from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet

# Create your views here.

def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

def tweets_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Purpose so we can consume by Javascript, or java, swift,etc.
    return json data
    """
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except: 
        raise Http404
    data={
        "id": tweet_id,
        "content": obj.content
    }
    return JsonResponse(data)