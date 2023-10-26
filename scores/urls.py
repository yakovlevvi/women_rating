from django.urls import path, include
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article_list'),
    path('upload_member/', views.AddPage.as_view(), name="upload_member"),
    path('<slug:article_slug>/update/', views.ScoresUpdateView.as_view(), name="article-update"),
    path('<int:pk>/delete/', views.ScoresDeleteView.as_view(), name="scores-delete"),
    # path('<slug:post_slug>', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.ScoresCategory.as_view(), name='category'),
    path('rate/<slug:article_slug>/', views.rate_article, name='rate_article')
]
