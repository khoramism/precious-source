import django_filters
from .models import Post 

class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {'title':['icontains'],
                'name':['icontains'],
                'stars': ['gt', 'lt'],
                'summary':['icontains'],
                }
    @property
    def qs(self):
        parent = super().qs
        return parent.filter(status=1) 