from django.shortcuts import render
from .models import Post
from .filters import PostFilter
from django.http import HttpResponse


def post_list(request, *args, **kwargs):
	object_list = Post.objects.filter()




from django.views import generic
from .models import Post


def post_list(request):
	posts = Post.objects.filter(status=1).order_by('-created')
	posts_count = posts.count()
	myFilter = PostFilter(request.GET, queryset=posts)
	filtered = myFilter.qs
	context = {'posts':posts, 'queryset_count':posts_count,'myFilter':myFilter,'filtered':filtered}
	return render(request, 'blog/post_list.html',context)

	
class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created')
	template_name = 'post_list.html'

class PostDetail(generic.DetailView):
	model = Post
	template_name = 'post_detail.html'

