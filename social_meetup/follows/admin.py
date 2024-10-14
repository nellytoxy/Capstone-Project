from django.contrib import admin
from .models import Follow

class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following', 'created_at')
    search_fields = ('follower__username', 'following__username')

    # Add a custom action for following/unfollowing
    actions = ['follow_users', 'unfollow_users']

    def follow_users(self, request, queryset):
        for follow in queryset:
            Follow.objects.get_or_create(follower=follow.follower, following=follow.following)
        self.message_user(request, "Users followed successfully.")

    def unfollow_users(self, request, queryset):
        for follow in queryset:
            Follow.objects.filter(follower=follow.follower, following=follow.following).delete()
        self.message_user(request, "Users unfollowed successfully.")

    follow_users.short_description = "Follow selected users"
    unfollow_users.short_description = "Unfollow selected users"

admin.site.register(Follow, FollowAdmin)

