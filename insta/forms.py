from django import forms
from .models import Image,Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["name"]

