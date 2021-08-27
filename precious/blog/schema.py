from .models import Post, Comment , LangTag, Category
from graphene_django import DjangoObjectType 
import graphene 
from django.shortcuts import get_object_or_404, get_list_or_404





class PostType(DjangoObjectType):
	class Meta:
		model = Post
		fields = '__all__'




class CommentType(DjangoObjectType):
	class Meta:
		model = Comment
		fields = '__all__'




class LangTagType(DjangoObjectType):
	class Meta:
		model = LangTag
		fields = '__all__'




class CategoryType(DjangoObjectType):
	class Meta:
		model = Category
		fields = '__all__'

class Query(graphene.ObjectType):
	post = graphene.List(PostType)


	comment = graphene.List(CommentType)
	
	post_by_slug = graphene.Field(PostType, slug =graphene.String(required=True))

	category = graphene.List(CategoryType)
	
	category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
	
	langtag = graphene.List(LangTagType)
	
	langtag_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

	def resolve_all_posts(root, info):
		# We can easily optimize query count in the resolve method
		return Post.objects.all()

	def resolve_all_comments(root, info):
		# We can easily optimize query count in the resolve method
		return Post.objects.select_related("category").all()
		

	def resolve_category_by_name(root, info, name):
		try:
			return Category.objects.get(name=name)
		except Category.DoesNotExist:
			return None

	def resolve_langtag_by_name(root, info, name):
		try:
			return LangTag.objects.get(name=name)
		except LangTag.DoesNotExist:
			return None

	def resolve_post_by_slug(root, info, slug):
		try:
			return Post.objects.get(slug=slug)
		except Post.DoesNotExist:
			return None
			
schema = graphene.Schema(query=Query)