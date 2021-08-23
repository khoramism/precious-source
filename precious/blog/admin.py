from django.contrib import admin
from .models import Post , Comment, Category, LangTag
from django import forms
from ckeditor.widgets import CKEditorWidget
# Register your models here.

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    #langtag = forms.MultipleChoiceField(widget=CustomCheckboxSelectMultiple, required=False)
    class Meta:
        model = Post
        fields = '__all__'



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'status','created','updated')
    form = PostAdminForm
    list_filter = ("status",)
    search_fields = ['title', 'content']
# Register your models here.

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(LangTag)