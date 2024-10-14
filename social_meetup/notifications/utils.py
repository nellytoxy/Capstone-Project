# notifications/utils.py
from .models import Notification

def send_follow_notification(followed_user, follower_user):
    message = f"{follower_user.username} started following you."
    Notification.objects.create(user=followed_user, message=message, notification_type='follow')

def send_like_notification(post, liker_user):
    message = f"{liker_user.username} liked your post."
    Notification.objects.create(user=post.user, message=message, notification_type='like')

def send_comment_notification(post, commenter_user, comment):
    message = f"{commenter_user.username} commented on your post: '{comment.content}'."
    Notification.objects.create(user=post.user, message=message, notification_type='comment')
