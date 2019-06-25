from django.db import models
from django.contrib.auth.models import User
import datetime as dt


class Profile(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length= 500, blank= True)
    profile_pic = models.ImageField(upload_to = 'images/', blank = True)

    def __str__(self):
        return self.first_name
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
    
    @classmethod
    def get_profiles(cls):
        all_profiles = cls.objects.all()
        return all_profiles
    
    @classmethod
    def get_profile_by_id(cls,id):
        profile = cls.objects.get(id = id)
        return profile
    
    @classmethod
    def search_profile(cls,search_item):
        sought_prof = cls.objects.get(name__username = search_item)
        return sought_prof

class Image(models.Model):
    image_caption = models.TextField()
    comments = models.ForeignKey('Comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/', default = 'gallery/media/images')
    posted = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length = 50)
    profile = models.ForeignKey('Profile')

    def __str__(self):
        return self.user.username

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    @classmethod
    def get_images(cls):
        all_images = cls.objects.all()
        return all_images
    
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.get(id = id)
        return image
    
    @classmethod
    def get_comments_by_image(cls):
        all_comments = Image.objects.get(comments__post).all()

class Comments(models.Model):
    post = models.CharField(max_length = 260, blank=True)
    posted_by = models.ForeignKey(User)
    posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.post
    
    def save_comment(self):
        self.save()

    def delete_comment(Self):
        self.delete()
        


class Followers(models.Model):
    pass

class Following(models.Model):
    pass