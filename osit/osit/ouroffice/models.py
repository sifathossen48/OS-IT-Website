from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


"""Ouroffice model"""

class Ouroffice(models.Model):
    name = models.CharField(max_length=30, unique=True)
    details = HTMLField(max_length=4000)

    def __str__(self):
        return self.name
    
    