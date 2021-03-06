from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import Image,Followers,Following,Profile,Comments
from .forms import ProfileForm,CommentsForm,ImageForm
from django.contrib.auth.models import User


@login_required(login_url='/accounts/login/')
def landing_page(request):
    images = Image.objects.all()
    # image = Image.objects.get()
    comments=Comments.objects.all()
    current_user = request.user
    # image = Image.objects.get(image=id)
    # form = CommentsForm()

    if request.method =="POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comm = form.save(commit = False)
            comm.posted_by = current_user
            comm.image = image
            comm.save()
        
            # return redirect(landing_page)
    else:
        form = CommentsForm()    

    return render(request, "all-out/index.html", {"images": images,"form":form,"comments":comments})


@login_required(login_url='/accounts/login/')
def profile(request,id):
    current_user = request.user
    profile = Profile.objects.get(name = id)
    images = Image.objects.all()

    # all_images = []
    # images = Image.objects.all()
    # def imge(images):
    #     for image in images:
    #         if image.user.id == profile.name.id:
    #             return image

        # return all_images  

    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.save()
    
    else:
        form = ImageForm()

    return render(request, "all-out/profile.html", {"profile":profile,"form":form,"images":images})


@transaction.atomic
def edit_profile(request):
    current_user = request.user
    # update = Profile.objects.filter(id = current_user.id)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
        
            return redirect('profile',current_user.id)
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, "all-out/edit_profile.html", {"form":form})

def search_results(request):
    if 'users' in request.GET and request.GET["users"]:
        search_term = request.GET.get("users")
        searched_users = Profile.search_profile(search_term)

        message = f"{ search_term }"

        return render(request,"all-out/search.html",{"message":message,"profile":searched_users})
    
    else:
        message = "You Haven't Searched For Anything Yet"

        return render(request,"all-out/search.html", {"message":message})
        
