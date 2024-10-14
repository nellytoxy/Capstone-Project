from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')
    list_filter = ('user', 'is_read')
    ordering = ('-created_at',)  # Show most recent first

admin.site.register(Notification, NotificationAdmin)
