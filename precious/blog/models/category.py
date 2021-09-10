from django.db import models 
from multiselectfield import MultiSelectField
from .choices import *


class Category(models.Model): 
    cats = MultiSelectField(choices=CATS)