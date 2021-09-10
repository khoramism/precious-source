from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator,URLValidator, EmailValidator
from .models import choices
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

class PostAdminForm(forms.ModelForm):
    cats = forms.MultipleChoiceField(label="", choices=choices.CATS, widget=forms.CheckboxSelectMultiple())
    langtags = forms.MultipleChoiceField(label="", choices=choices.LANGTAGS, widget=forms.CheckboxSelectMultiple())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['summary'].required = True
        self.fields['content'].required = True
        self.fields['title'].required = True
        self.fields['url'].required = True
    class Meta:
        model = Post
        fields = '__all__'

class InsertionAdminForm(forms.ModelForm):
    
    cats = forms.MultipleChoiceField(label="", choices=choices.CATS, widget=forms.CheckboxSelectMultiple())
    langtags = forms.MultipleChoiceField(label="", choices=choices.LANGTAGS, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Insertion
        fields = '__all__'



class SearchForm(forms.Form):
    search = forms.CharField(required=False, label="")
    search.widget = forms.TextInput(attrs={'placeholder':"تایپ کنید: ",'name': 'email'})

class TableSearchForm(forms.Form):
    cats = forms.MultipleChoiceField(label="", choices=choices.CATS, widget=forms.CheckboxSelectMultiple())
    langtags = forms.MultipleChoiceField(label="", choices=choices.LANGTAGS, widget=forms.CheckboxSelectMultiple())
    stars = forms.IntegerField(label="ستاره ها")
    
class InsertionForm(forms.ModelForm):
    cats = forms.MultipleChoiceField(label="", choices=choices.CATS, widget=forms.CheckboxSelectMultiple())
    langtags = forms.MultipleChoiceField(label="", choices=choices.LANGTAGS, widget=forms.CheckboxSelectMultiple())
    your_email = forms.EmailField(label=_("ایمیل شما دوست عزیز "))
    project_link = forms.URLField(label = _('لینک پروژه شما ای دوست گل :'))
    class Meta:
        model = Insertion
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(InsertionForm, self).__init__(*args, **kwargs)
        self.fields['project_link'].help_text = _('یک لینکی استفاده کن که به .git ختم شه گل !')
        self.fields['project_link'].label = _('لینک پروژه')
        self.fields['project_link'].validators.append(RegexValidator(
            regex=r'^\/([^/]+)\/([^/]+).git(/[^#]+)?(#(.*))?$',
            message='باید یک پروژه گیت باشه گل!',
        ))
        self.fields['project_link'].validators.append(URLValidator(schemes=['http', 'https']))
        self.fields['your_email'].validators.append(EmailValidator(message = _('please provide a valid email.')))
