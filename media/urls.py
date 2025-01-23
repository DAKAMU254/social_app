from django.urls import path
from .views import HomeView, PostCreateView, PostDeleteView, CommentCreateView
from . import views  # Add this line to import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    path('delete_post/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),
    path('comment/<int:post_id>/', CommentCreateView.as_view(), name='comment_post'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
    path('followers/<int:user_id>/', views.user_followers_view, name='user_followers'),
    path('following/<int:user_id>/', views.user_following_view, name='user_following'),
    path('search/', views.search_users, name='search_users'),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
    path('toggle-follow/<int:user_id>/', views.toggle_follow, name='toggle_follow'),
]