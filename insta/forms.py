from django import forms
from .models import Image,Profile,Comments

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["name","images"]
    
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ["comments","user"]

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ["posted","posted_by"]

