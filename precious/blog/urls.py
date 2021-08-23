from django.urls import path
from . import views 
from .feeds import LatestPostsFeed
urlpatterns = [
    #path('', views.PostList.as_view(), name='post_list'),
    path('',views.post_list, name='post_list'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
]