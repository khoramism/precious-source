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


LANGTAGS = (
    ('Python','Python'),
    ('Java','Java'),
    ('JavaScript','JavaScript'), 
    ('Php','Php'),
    ('Wordpress','Wordpress'),
    ('BootStrap','BootStrap'),
    ("Html & Css","Html & Css"),
    ('SQLite','SQLite'),
    ('MySQL','MySQL'),
    ('PostgreSQL','PostgreSQL'),
    ('C#','C#'),
    ('Git','Git'),
    ('Docker','Docker'),
    ('Sass','Sass'),
    ('Scss','Scss'),
    ('R','R'),
    ('Kotlin','Kotlin'),
    ('Go','Go'),
    ('C++','C++'),
    ('C','C'),
    ('JSON(API)','JSON(API)'),
    ('Ajax','Ajax'),
    ('AngularJS','AngularJS'),
    ("React","React"),
    ('JQuery','JQuery'),
    ('Vue','Vue'),
    ('Node.js','Node.js'),
    ('Raspberrypi','Raspberrypi'),
    ('ASP','ASP'),
    ('Django','Django'),
    ('Express.js','Express.js'),
    ('Flask','Flask'),
    ('CherryPy','CherryPy'),
    ('GraphQL','GraphQL'),
    ('TensorFlow','TensorFlow'),
    ('Pandas','Pandas'),
    ('Numpy','Numpy'),
    ('PyTorch','PyTorch'),
    ('Keras','Keras'),
    ('Theano','Theano'),
    ('MatPlotLib','MatPlotLib'),
    ('SciPy','SciPy'),
    ('PyGame','PyGame'),
    ('BS4','BS4'),
    ('Pillow','Pillow'),
    ('Meteor','Meteor'),
    ('Next.js','Next.js'),
    ('Ionic','Ionic'),
    ('Winjs','Winjs'),
    ('Selenium','Selenium'),
    ('OpenCV','OpenCV'),
    ("Dojo","Dojo"),
    ('Velocity.js','Velocity.js'),
    )

CATS = (
    ("Artificial Intelligence and Machine Learning","Artificial Intelligence and Machine Learning"),
    ("Security","Security"),
    ("Data Science/Analytics","Data Science/Analytics"),
    ("Software Development", "Software Development"),
    ("Computer Networking", "Computer Networking"),
    ("Frontend Development","Frontend Development"),
    ("Backend development", "Backend development"),
    ("Mobile Development", "Mobile Development"),
    ("Desktop Development", "Desktop Development"),
    ("DevOps Development","DevOps Development"),
    ("Game Development","Game Development"),
    ("Web Development","Web Development"),
    ("Cryptography Development","Cryptography Development"),
    ("CryptoCurrnecy Development","CryptoCurrnecy Development"),
    ("BlockChain Development","BlockChain Development"),
    ("Database Development",  "Database Development"),

)

class SearchForm(forms.Form):
    search = forms.CharField(required=False, label="")
    search.widget = forms.TextInput(attrs={'placeholder':"تایپ کنید: ",'name': 'email'})

class TableSearchForm(forms.Form):
    cats = forms.MultipleChoiceField(label="", choices=CATS, widget=forms.CheckboxSelectMultiple())
    langtags = forms.MultipleChoiceField(label="", choices=LANGTAGS, widget=forms.CheckboxSelectMultiple())
    stars = forms.IntegerField(label="ستاره ها")
    
