from django.db import models 


class Base(models.Model):
	STATUS = (
		('draft', 'در حال انتظار'),
		('published', 'منتشر شده'),
		)

	created = models.DateTimeField(auto_now_add = True, verbose_name='ساخت',null=True)

	updated = models.DateTimeField(auto_now = True,verbose_name='آپدیت')

	status = models.CharField(max_length=60, choices = STATUS, default='draft', verbose_name='وضعیت')
	
	class Meta:
		abstract = True