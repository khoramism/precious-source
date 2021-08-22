
# Create your models here.
from django.db import models
from .base import Base
from .category import Category
from ckeditor_uploader.fields import RichTextUploadingField


class Post(Base):
	title = models.CharField(max_length=25)
	
	name  = models.CharField(max_length=25)

	url = models.URLField(max_length=100)

	stars = models.IntegerField(default=0)

	content = RichTextUploadingField(blank=True)
	
	summary = models.CharField(max_length=300,blank=True,null=True,default='')

	cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
	
	video = models.URLField(max_length=1000)
	
	def __str__(self):
		return self.title
	
	class Meta:	
		ordering = ['-created']