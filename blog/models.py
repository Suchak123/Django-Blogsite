from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)#date for creation
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

