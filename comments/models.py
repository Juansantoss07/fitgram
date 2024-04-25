from django.db import models
from publish.models import Posts
from customUser.models import Usuario
from django.utils import timezone
# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.DO_NOTHING)
    user_comment = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    comment = models.CharField(max_length=900)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment