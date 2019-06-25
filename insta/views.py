from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import Image,Followers,Following,Profile,Comments
from .forms import ProfileForm,CommentsForm,ImageForm


@login_required(login_url='/accounts/login/')
def landing_page(request):
    images = Image.objects.all()
    current_user = request.user
    form = CommentsForm()

    if request.method =="POST":
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            comm = form.save(commit = False)
            comm.posted_by = current_user
            comm.save()
        
            # return redirect(landing_page)
    else:
        form = CommentsForm()
    

    return render(request, "all-out/index.html", {"images": images,"form":form})


@login_required(login_url='/accounts/login/')
def profile(request,id):
    current_user = request.user
    profile = Profile.objects.get(id = current_user.id)
    
    images = Image.objects.all()
    all_images = []
    for image in images:
        if image.profile.name == current_user:
            all_images.append(image)
            

        print(all_images)    

    return render(request, "all-out/profile.html", {"profile":profile,"images":all_images})


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            proform = form.save(commit=False)
            current_user.username = proform.new_username
            update = Profile.objects.get(current_user.id)
            
            update.save()
        
            return redirect(profile)
    else:
        form = ProfileForm()

    return render(request, "all-out/edit_profile.html", {"form":form, "current":current_user})
