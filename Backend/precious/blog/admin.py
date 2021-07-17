from django.contrib import admin
from .models import Post 
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'status','created','updated')

# Register your models here.

admin.site.register(Post, PostAdmin)