from django.contrib import admin
from .models import Post , Comment, Category
from django import forms
from ckeditor.widgets import CKEditorWidget

# Register your models here.

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'status','created','updated')
    form = PostAdminForm
# Register your models here.

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)
admin.site.register(Category)