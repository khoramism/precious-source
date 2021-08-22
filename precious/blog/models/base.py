from django.db import models 
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Base(models.Model):
	
	created = models.DateTimeField(auto_now_add = True, verbose_name='ساخت',null=True)

	updated = models.DateTimeField(auto_now = True,verbose_name='آپدیت')

	status = models.CharField(max_length=60, choices = STATUS, default='draft', verbose_name='وضعیت')
	
	class Meta:
		abstract = True