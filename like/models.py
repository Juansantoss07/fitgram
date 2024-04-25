from django.db import models
from publish.models import Posts
from django.conf import settings
# Create your models here.
class Like(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.DO_NOTHING)
    user_like = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    like = models.IntegerField()
    color_icon = models.CharField(max_length=10, default='none')  # Nova coluna para armazenar a cor do ícone

    def __str__(self):
        return str(self.like).count()