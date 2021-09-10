from django.contrib import admin
from .models import Post ,Insertion, Comment, Category, LangTag
from django import forms
from ckeditor.widgets import CKEditorWidget
from .forms import PostAdminForm, InsertionAdminForm
# Register your models here.



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'status','created','updated')
    #form = PostAdminForm
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(Insertion)
class InsertionAdmin(admin.ModelAdmin):
    list_display = ('your_email','project_link')
    #form = InsertionAdminForm
    search_fields = ('your_email','project_link')


admin.site.register(Category)
admin.site.register(LangTag)