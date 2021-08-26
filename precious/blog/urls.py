from django.urls import path
from . import views 
from .feeds import LatestPostsFeed
urlpatterns = [
    #path('', views.PostList.as_view(), name='post_list'),
    path('',views.post_list, name='post_list'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('hank', views.search_forms, name='search_forms'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
]