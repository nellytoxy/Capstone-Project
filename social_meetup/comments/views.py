from rest_framework import permissions, status, viewsets, generics
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from posts.models import Post
from user_profile.permissions import IsOwnerOrReadOnly
from notifications.utils import send_comment_notification

class CommentViewSet(viewsets.ModelViewSet):
    """Comments API viewset"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Save the comment with the user as the owner
        serializer.save(user=self.request.user)  # Ensure you're using the correct field name here

class CommentPostView(generics.CreateAPIView):
    """API view to create a comment for a specific post"""
    serializer_class = CommentSerializer  # Optional: You can specify the serializer if you need validation

    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        # Validate the content is provided
        content = request.data.get('content')
        if not content:
            return Response({'error': 'Content is required'}, status=status.HTTP_400_BAD_REQUEST)

        comment = Comment.objects.create(user=request.user, post=post, content=content)
        
        # Send notification
        send_comment_notification(post, request.user, comment)
        
        return Response({'id': comment.id}, status=status.HTTP_201_CREATED)
