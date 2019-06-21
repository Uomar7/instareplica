from django.contrib import admin
from .models import Followers,Following,Profile,Comments,Image

admin.site.register(Image)
admin.site.register(Comments)
admin.site.register(Followers)
admin.site.register(Following)
admin.site.register(Profile)
