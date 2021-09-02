from django.shortcuts import render
import json
from django.core import serializers
from .models import SearchHistory

# Create your views here.

def serchStory(request):
    searchStories = SearchHistory.objects.all()
    dataJson = serializers.serialize("json",searchStories)
    return render(request,"index.html",{"data":dataJson})