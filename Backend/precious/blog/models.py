from django.db import models

# Create your models here.
class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'در حال انتظار'),
		('published', 'منتشر شده'),
	)
	
	title = models.CharField(max_length=25)
	
	content = models.TextField()
	
	#summary = models.CharField(max_length=300,blank=True,null=True,default='')


	created = models.DateTimeField(auto_now_add = True, verbose_name='ساخت',null=True)

	updated = models.DateTimeField(auto_now = True,verbose_name='آپدیت')

	status = models.CharField(max_length=60, choices = STATUS_CHOICES, default='draft', verbose_name='وضعیت')
	
	def __str__(self):
		return self.title
		

