# Generated by Django 5.0.4 on 2024-04-24 18:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0004_posts_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='likes',
        ),
        migrations.AddField(
            model_name='posts',
            name='likes',
            field=models.ManyToManyField(related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
