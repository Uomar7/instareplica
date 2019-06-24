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
