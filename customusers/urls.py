from django.urls import path, include
from .views import *

urlpatterns = [
    path('', user_list, name='user_list'),
    path('<str:username>', UserScores.as_view(), name='user_scores'),
    # path('<str:username>/posts', UserScores.as_view(), name='user_scores'),
]
