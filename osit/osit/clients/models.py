from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


"""Clients model"""

class Clients(models.Model):
    image = ResizedImageField(size=[300, 300], quality=75, upload_to="client_images/", force_format='WEBP')
    
    def __str__(self):
        return "{}".format(self.image)
    

