from django.urls import path
from . import views
from scores.views import ShowPost

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('user_ratings_list/', views.UserScores.as_view(), name='user_ratings_list'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),  # !CHECK
    path('<str:username>/', views.UserProfileView.as_view(slug_field='username'), name='user_profile'),
    # path('<str:username>/', ProfileView.as_view(slug_field='username'), name='user_rating'),
]
