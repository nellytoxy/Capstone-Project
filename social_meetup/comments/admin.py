from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'created_at')  # Display columns
    search_fields = ('user__username', 'post__title', 'content')  # Enable searching
    list_filter = ('post', 'user', 'created_at')  # Add filters

admin.site.register(Comment, CommentAdmin)
