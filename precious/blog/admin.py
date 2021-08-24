from django.contrib import admin
from .models import Post , Comment, Category, LangTag
from django import forms
from ckeditor.widgets import CKEditorWidget
# Register your models here.

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    #langtag = forms.MultipleChoiceField(widget=CustomCheckboxSelectMultiple, required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['summary'].required = True
        self.fields['content'].required = True
        self.fields['title'].required = True
        self.fields['url'].required = True
    class Meta:
        model = Post
        fields = '__all__'



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'status','created','updated')
    form = PostAdminForm
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
# Register your models here.

admin.site.register(Post, PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Category)
admin.site.register(LangTag)