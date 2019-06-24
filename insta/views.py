from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import Image,Followers,Following,Profile
from .forms import ProfileForm


@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()   
    return render(request,'all-out/index.html',{"images":images})

@login_required(login_url='/accounts/login/')
def edit_profile(request):

    current_user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            details = form.save(commit=False)
            details.user = current_user
            details.save()

        else:
            form = ProfileForm()

        return render(request, 'all-out/edit_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def profile_page(request):
    info = Profile.objects.all()

    return render(request, "profile.html",{"info":info})
