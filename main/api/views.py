from django.shortcuts import render
from rest_framework import viewsets
from Content.models import Posts
from .serializers import PostsThemeSerializer
# Create your views here.

class PostsThemeViewApi(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsThemeSerializer
    