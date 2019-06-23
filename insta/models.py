from django.db import models
from django.contrib.auth.models import User
import datetime as dt

class Image(models.Model):
    image_caption = models.TextField()
    comments = models.CharField(max_length = 280, blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images', default = 'gallery/media/images')
    posted = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length = 50)

    def __str__(self):
        return self.image

class Profile(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length= 500, blank= True)
    profile_pic = models.ImageField(upload_to = 'image', blank = True)
    age = models.DateField(blank = True)

    def __str__(self):
        return self.first_name

class Followers(models.Model):
    name = models.ForeignKey(User)
    def __str__(self):
        return self.name

class Following(models.Model):
    name = models.ForeignKey(User)
    def __str__(self):
        return self.name