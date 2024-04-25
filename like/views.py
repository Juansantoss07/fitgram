from django.shortcuts import render, redirect
from publish.models import Posts
from customUser.models import Usuario
from .models import Like
# Create your views here.
def add_like(request, id_post):
    if request.method == "POST":
        post = Posts.objects.get(id=id_post)
        user = Usuario.objects.get(id=request.user.id)

        try:
            # Verifica se o usuário já curtiu o post
            like_obj = Like.objects.get(post=post, user_like=user)
            # Se já curtiu, remove o like e atualiza a cor do ícone
            like_obj.delete()
        except Like.DoesNotExist:
            # Se o usuário ainda não curtiu o post, cria um novo objeto Like
            like_obj = Like.objects.create(post=post, user_like=user, like=1)
            # Define a cor do ícone como 'like'
            like_obj.color_icon = 'like'
            like_obj.save()  # Salva as alterações no banco de dados

    return redirect('/publish/home')
