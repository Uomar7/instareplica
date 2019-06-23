from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image,Followers,Following


@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()   
    return render(request,'all-out/index.html',{"images":images})
