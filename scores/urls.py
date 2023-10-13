from django.urls import path, include
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', views.ScoresHome.as_view(), name='scores_home'),
    path('upload_member', views.AddPage.as_view(), name="upload_member"),
    path('<int:pk>/update', views.ScoresUpdateView.as_view(), name="scores-update"),
    path('<int:pk>/delete', views.ScoresDeleteView.as_view(), name="scores-delete"),
    path('<slug:post_slug>', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', views.ScoresCategory.as_view(), name='category'),

]
