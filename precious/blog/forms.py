from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
'''
class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(),required=True, max_length=100)
    content = RichTextField()

    class Meta:
        model  = Post
        fields = ('title','content',)
'''
class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(config_name='comments'),required=True, max_length=2048)
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    search = forms.CharField(required=False, label="")
    search.widget = forms.TextInput(attrs={'placeholder':"تایپ کنید: ",'name': 'email'})