from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField



"""News model"""

class News(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField(max_length=4000)  
    news = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    starter = models.ForeignKey(User, related_name='news', on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    image = ResizedImageField(size=[300, 300], quality=75, upload_to="news_images/", force_format='WEBP', blank=True)
    
    def __str__(self):
        return "{} - {} - {}".format(self.title, self.details, self.image)




