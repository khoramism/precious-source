import django_filters
from .models import Post 
from django import forms 

class PostFilter(django_filters.FilterSet):
    '''langtag = django_filters.CharFilter(
        widget=forms.CustomCheckboxSelectMultiple(attrs={
            'btn_class': 'btn btn-link dccn-link dccn-text-small',
            'label_class': 'lang-tag-filter',
        })
    )
'''
    class Meta:
        model = Post
        fields = {'title':['icontains'],
                'name':['icontains'],
                'stars': ['gt', 'lt'],
                'summary':['icontains'],
                'cat':['exact'],
                'langtag':['exact'],
                }
    @property
    def qs(self):
        parent = super().qs
        return parent.filter(status=1) 