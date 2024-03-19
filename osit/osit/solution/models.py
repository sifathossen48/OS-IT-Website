from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


"""Solution model"""

class Solution(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
    

"""Product model"""

class Product(models.Model):
    name = models.CharField(max_length=255)
    solution = models.ForeignKey(Solution, related_name='product', on_delete=models.CASCADE)
    image = ResizedImageField(size=[300, 300], quality=75, upload_to="product_images/", force_format='WEBP', blank=False)
    
    def __str__(self):
        return "{} - {} - {}".format(self.name, self.image)