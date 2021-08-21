
# Create your models here.
from django.db import models
from .base import Base
from .category import Category
from ckeditor_uploader.fields import RichTextUploadingField

class Post(Base):
	title = models.CharField(max_length=25)
	
	content = RichTextUploadingField(blank=True)
	
	summary = models.CharField(max_length=300,blank=True,null=True,default='')

	cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
	
	def __str__(self):
		return self.title
		