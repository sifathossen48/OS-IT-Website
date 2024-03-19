from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from tinymce.models import HTMLField


"""Ourteam model"""

class Ourteam(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
    
    def get_members_count(self):
        return Teammember.objects.filter(ourteam=self).count()
    

"""Teammember model"""

class Teammember(models.Model):
    name = models.CharField(max_length=255)
    details = HTMLField(max_length=4000) 
    ourteam = models.ForeignKey(Ourteam, related_name='teammember', on_delete=models.CASCADE)
    image = ResizedImageField(size=[300, 300], quality=75, upload_to="member_images/", force_format='WEBP', blank=True)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.details, self.image)
    


