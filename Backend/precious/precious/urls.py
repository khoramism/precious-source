from django.contrib import admin
from django.urls import path, include , re_path
from django.urls.conf import re_path
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostView, 'post-view')

urlpatterns = patterns(
    'talk.views',
    url(r'^$', 'home'),

    # api
    url(r'^api/v1/posts/$', 'post_collection'),
    url(r'^api/v1/posts/(?P<pk>[0-9]+)$', 'post_element')
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('post.urls')),
    re_path(r'^api/v1/posts/$', 'post_collection'),
    re_path(r'^api/v1/posts/(?P<pk>[0-9]+)$', 'post_element')
]