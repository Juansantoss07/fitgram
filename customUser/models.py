from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    foto_perfil = models.ImageField(upload_to='perfil')