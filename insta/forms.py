from django import forms
from .models import Image,Profile,Comments
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["name"]
    
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ["comments","user","profile"]

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ["posted","posted_by"]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        fields = ["username","email"]