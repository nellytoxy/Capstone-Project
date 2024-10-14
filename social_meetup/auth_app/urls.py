from django.urls import path
from auth_app.views import FeedView  # Adjust the import based on your project structure
from .views import RegisterView, LoginView, LogoutView
from posts.models import Post

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('feed/', FeedView.as_view({'get': 'list'}), name='feed'),  # Adjust if using ViewSets
]
