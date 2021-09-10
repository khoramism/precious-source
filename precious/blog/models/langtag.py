from django.db import models
from multiselectfield import MultiSelectField
from django.utils.translation import ugettext_lazy as _
from .choices import *



class LangTag(models.Model):
    langtags = MultiSelectField(choices=LANGTAGS)
