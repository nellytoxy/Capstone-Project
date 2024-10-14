from django.utils import timezone
from comments.models import Comment  # Adjust the import based on your structure

# Update existing comments to have a default created_at value
Comment.objects.filter(created_at__isnull=True).update(created_at=timezone.now())
