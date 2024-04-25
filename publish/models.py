from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    post_image = models.ImageField(upload_to='posts')
    user_post = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.title
        