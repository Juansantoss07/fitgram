# Generated by Django 5.0.4 on 2024-04-24 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0002_posts_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='likes',
        ),
    ]
