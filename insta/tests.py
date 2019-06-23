from django.test import TestCase
from .models import Image,Followers,Following,Comments,Profile

class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image(image_name = me, image_caption = "Hey nice",user = "Umar", location =  )
