from django.db import models
from .category import Category
from .langtag import LangTag

class Insertion(models.Model):
    project_link = models.URLField(verbose_name='لینک پروژه شما')
    
    your_email  = models.EmailField(verbose_name='ایمیل شما :)')

    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='insertions')

    langtags = models.ForeignKey(LangTag, on_delete=models.CASCADE, related_name='insertions')

    