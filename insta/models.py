from django.db import models

class image(models.Model):
    image_name = models.CharField(max_length = 40)
    image_caption = models.TextField()
    likes = models.
