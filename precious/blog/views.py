from django.shortcuts import render, reverse,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q 
from django.utils.translation import gettext_lazy as _

from django.views import generic
# POSTGRESQL 
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

# Internal imports 
from .models import Post, Comment
from .filters import PostFilter
from .forms import CommentForm, SearchForm,TableSearchForm, InsertionForm

def post_list(request):
	## WITHOUT THE POSTGRESQL VECTOR SEARCH
	posts = Post.objects.filter(status='published').order_by('-created')
	if 'search' in request.GET:
		form = SearchForm(request.GET)
		if form.is_valid():
			cd = form.cleaned_data['search']
			search_result = posts.filter(Q(title__icontains = cd ) | Q(summary__icontains = cd ) |Q(content__icontains= cd ))

		else: 
			search_result = ' مقاله ای یافت نشد'
	else: 
		form = SearchForm(request.GET)
		search_result = ' مقاله ای یافت نشد'

	all_posts_count = posts.count()
	myFilter = PostFilter(request.GET, queryset=posts)
	filtered = myFilter.qs	
	# PAGINGATION
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



	
	if request.method == 'POST':
		myform = TableSearchForm(request.POST)
		if myform.is_valid():
			cats = form.cleaned_data.get('cats')
			langtags = form.cleaned_data.get('langtags')
			stars = form.cleaned_data.get('stars')
			# do something with your results
			#table_search_results = posts.filter(Q(title__icontains = cd ) | Q(summary__icontains = cd ) |Q(content__icontains= cd ))
			print(stars)
			print(langtags)
			print(cats)
	else:
		myform = TableSearchForm

	

	context = {'all_posts_count':all_posts_count,'page': page,'myFilter':myFilter,'filtered':filtered, 'search_result':search_result,'form':form , 'myform':myform}
	return render(request, 'blog/post_list.html',context)


def post_detail(request, slug):
	template_name = 'blog/post_detail.html'
	post = get_object_or_404(Post, slug=slug)
	comments = post.comments.filter(active=True)
	new_comment = None
	# Comment posted
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():

			# Create Comment object but don't save to database yet
			new_comment = comment_form.save(commit=False)
			# Assign the current post to the comment
			new_comment.post = post
			# Save the comment to the database
			new_comment.save()
	else:
		comment_form = CommentForm()

	return render(request, template_name, {'post': post,
										   'comments': comments,
										   'new_comment': new_comment,
										   'comment_form': comment_form})

def search_forms(request):
	return render(request, 'blog/search_forms.html',{})

class CreateInsertionView(generic.CreateView):
	model  = Post
	form_class = InsertionForm
	template_name = 'blog/insertion_create.html'


class ContactsView(generic.TemplateView):
	template_name = 'blog/contacts.html'



class SupportView(generic.TemplateView):
	template_name = 'blog/support.html'