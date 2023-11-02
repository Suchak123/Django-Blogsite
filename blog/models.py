from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)#date for creation
    author = models.ForeignKey(User , on_delete=models.CASCADE)

    date_modified = models.DateTimeField(auto_now=True)