from django.db import models

# Create your models here.
from rest_framework import viewsets
from posts.models import Post  
from posts.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import serializers
from .models import Post  # Ensure you're importing Post from the correct location


class FeedView(viewsets.ViewSet):
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
