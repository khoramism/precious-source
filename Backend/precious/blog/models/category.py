from django.db import models 
from .base import Base

class Category(Base):
    name = models.CharField(max_length=20)