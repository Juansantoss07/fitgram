from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Comment
from publish.models import Posts
from customUser.models import Usuario
# Create your views here.
def add_comment(request, id_post):
    if request.method == "GET":
        return render(request, 'add_comment.html', {'id_post': id_post})

    elif request.method == "POST":
        user = Usuario.objects.get(id=request.user.id)
        comment = request.POST.get('comment')
        post = Posts.objects.get(id=id_post)
        commentTable = Comment(
            post = post,
            user_comment = user,
            comment = comment
        )

        commentTable.save()

    return redirect('/publish/home')