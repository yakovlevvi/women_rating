from django.urls import path
from .views import *
from scores.views import ShowPost

app_name = 'users'

urlpatterns = [
    path('', user_list, name='user_list'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('user_ratings_list/', UserScores.as_view(), name='user_ratings_list'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('<str:username>/', UserProfileView.as_view(slug_field='username'), name='user_profile'),
    # path('<str:username>/', ProfileView.as_view(slug_field='username'), name='user_rating'),
]
