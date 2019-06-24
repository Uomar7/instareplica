from django.contrib import admin
from .models import Followers,Following,Profile,Image,Comments

admin.site.register(Image)
admin.site.register(Followers)
admin.site.register(Following)
admin.site.register(Profile)
admin.site.register(Comments)
