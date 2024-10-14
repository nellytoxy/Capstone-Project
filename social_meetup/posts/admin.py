from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('owner', 'content', 'post_date', 'category')  # Columns to display in the list view
    search_fields = ('owner__username', 'content', 'category')  # Enable searching by username and content
    list_filter = ('category', 'post_date')  # Add filters in the right sidebar

admin.site.register(Post, PostAdmin)

