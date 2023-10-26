from django.urls import path, include
from .views import *
from scores.views import ShowPost

urlpatterns = [
    path('', user_list, name='user_list'),
    path('user_ratings_list/', UserScores.as_view(), name='user_ratings_list'),
    path('user/<str:username>/', UserProfileView.as_view(slug_field='username'), name='user_profile'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    # path('<str:username>/', ProfileView.as_view(slug_field='username'), name='user_rating'),
]
