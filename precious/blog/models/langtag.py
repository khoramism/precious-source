from django.db import models

from django.utils.translation import ugettext_lazy as _


'''langtags = (
    ('Django',_('Django'))
    ('Python',_('Python'))
    ('C#',_('C#'))
    ('.Net',_('.Net'))
    ('Laravel',_('Laravel'))
    ('Php',_('Php'))
    ('Java',_('Java'))
    ('JavaScript',_('JavaScript'))
    ('express.js',_('express.js'))
    ('Node.js',_('Node.js'))
)
'''
class LangTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name