from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Follow
from .serializers import FollowSerializer

class FollowViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = FollowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(follower=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            follow = Follow.objects.get(pk=pk, follower=request.user)
            follow.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Follow.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# follows/views.py
from rest_framework import generics
from .models import Follow
from notifications.utils import send_follow_notification
from django.contrib.auth.models import User

class FollowUserView(generics.CreateAPIView):
    def post(self, request, user_id):
        followed_user = User.objects.get(id=user_id)
        follow = Follow.objects.create(user=request.user, following=followed_user)
        
        # Send notification
        send_follow_notification(followed_user, request.user)
        
        return Response({'message': 'Following successfully!'})
