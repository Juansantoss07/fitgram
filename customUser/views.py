from django.shortcuts import render, redirect
from customUser.models import Usuario
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth
import re

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    
    if request.user.is_authenticated:
        return redirect('/publish/home')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password') 
        
        user = auth.authenticate(request, username=username, password=password)
        
        if user:
            auth.login(request, user)
            return redirect('/publish/home')
        
        messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
        return redirect('/usuarios/login')
    
def register(request):
    if request.method == "GET":
        
        return render(request, 'register.html')
    
    elif request.method == "POST":
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        foto = request.FILES.get('photo')
        
        if not re.search(r'\d', password) or not re.search(r'[a-zA-Z]', password):
            messages.add_message(request, messages.ERROR, 'A senha deve conter pelo menos uma letra e um número.')
            return redirect('/usuarios/register')

        if len(password) < 8:
            messages.add_message(request, messages.ERROR, 'A senha deve ter no mínimo 8 caracteres.')
            return redirect('/usuarios/register')
        
        user = Usuario.objects.create_user(
            email=email,
            first_name=firstname,
            last_name=lastname,
            username=username,
            password=password,
            foto_perfil=foto
        )

    messages.add_message(request, messages.SUCCESS, 'Seja bem vindo a nossa plataforma! Faça login para entrar.')
    return redirect('/usuarios/login')

def logout(request):
    auth.logout(request)
    return redirect('/usuarios/login')