from django.shortcuts import render, redirect
from .models import Posts
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    if request.method == "GET":
        posts = Posts.objects.all().order_by('-created_at')
        
        return render(request, 'home.html',  {'posts':posts})
    
    if request.method == "POST":
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        location = request.POST.get('location')
        image = request.FILES.get('photo')
        user = request.user

    posts = Posts(
        title = title,
        subtitle = subtitle,
        location = location,
        post_image = image,
        user_post = user,
    )

    posts.save()
    
    messages.add_message(request, constants.SUCCESS, 'Post criado com sucesso!')
    return redirect('/publish/home')


    
