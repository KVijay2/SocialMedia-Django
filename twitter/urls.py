from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('profile-list', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('profile/followers/<int:pk>', views.followers, name='followers'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_user, name='register'),
    path('search', views.search_results, name='search_results'),
    path('update_user/', views.update_user, name='update_user'),    
    path('tweet_like/<int:pk>', views.tweet_like, name="tweet_like"),
    path('tweet_share/<int:pk>', views.tweet_show, name="tweet_share"),
    path('unfollow/<int:pk>', views.unfollow, name="unfollow"),
    path('follow/<int:pk>', views.follow, name="follow"),
]
