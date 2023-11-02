from django.db import models


class User(models.Model):
    fname = models.CharField(max_length=50, blank=False)
    lname = models.CharField(max_length=50, blank=False) 
    email = models.EmailField(max_length=100, help_text='Email ID')
    passwd = models.CharField(max_length=50)
    age = models.IntegerField()


    def __str__(self):
        return self.fname + ' ' + self.lname
# Create your models here.
