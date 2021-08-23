from django.shortcuts import render, reverse
from .models import Post
from .filters import PostFilter
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def post_list(request, *args, **kwargs):
	object_list = Post.objects.filter()




from django.views import generic
from .models import Post


def post_list(request):
	posts = Post.objects.filter(status='published').order_by('-created')
	all_posts_count = posts.count()
	myFilter = PostFilter(request.GET, queryset=posts)
	filtered = myFilter.qs	
	paginator = Paginator(filtered, 3)  # 3 posts in each page
	page = request.GET.get('page')
	try:
		post_list = paginator.page(page)
	except PageNotAnInteger:
			# If page is not an integer deliver the first page
		post_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range deliver last page of results
		post_list = paginator.page(paginator.num_pages)

	context = {'all_posts_count':all_posts_count,'page': page,'myFilter':myFilter,'filtered':filtered}
	return render(request, 'blog/post_list.html',context)

	
class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created')
	template_name = 'post_list.html'

class PostDetail(generic.DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

