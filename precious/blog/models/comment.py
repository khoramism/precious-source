from .base import Base 

from ckeditor_uploader.fields import RichTextUploadingField

class Comment(Base):
    content = RichTextUploadingField(blank = False, config_name='comments')