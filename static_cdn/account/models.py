from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# class User(models.Model):
#     fname = models.CharField(max_length=50, blank=False)
#     lname = models.CharField(max_length=50, blank=False) 
#     email = models.EmailField(max_length=100, help_text='Email ID')
#     passwd = models.CharField(max_length=50)
#     age = models.IntegerField()


#     def __str__(self):
#         return self.fname + ' ' + self.lname
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)