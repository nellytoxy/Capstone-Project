from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import BlacklistTokenUpdateView
from votes.views import VoteViewSet
from comments.views import CommentViewSet
from posts.views import PostViewSet
from users.views import UserViewSet
from user_profile.views import ProfileViewSet
from friends.views import FriendViewSet
from follows.views import FollowViewSet
from notifications.views import NotificationListView  # Ensure you have this import

router = DefaultRouter()

# Register existing viewsets with the router
router.register(r'users', UserViewSet, basename='users')
router.register(r'profiles', ProfileViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'votes', VoteViewSet)
router.register(r'friends', FriendViewSet, basename='friends')

# Define the urlpatterns
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist'),
    
    # Follow/Unfollow endpoints
    path('follow/', FollowViewSet.as_view({'post': 'create'}), name='follow'),
    path('unfollow/<int:pk>/', FollowViewSet.as_view({'delete': 'destroy'}), name='unfollow'),
    
    # Notifications endpoint
    path('notifications/', NotificationListView.as_view(), name='notification_list'),
]

# Combine router URLs with urlpatterns
urlpatterns += router.urls
