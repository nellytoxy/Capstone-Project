from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from django.utils import timezone

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(default='')
    created_at = models.DateTimeField(null=True)  # Temporarily allow nulls

    def __str__(self):
        return f"{self.user.username} on {self.post.title}"
