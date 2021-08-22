from django.urls import path
from . import views 
urlpatterns = [
    #path('', views.PostList.as_view(), name='post_list'),
    path('',views.post_list, name='post_list'),
    path('<id:pk/', views.PostDetail.as_view(), name='post_detail'),
]