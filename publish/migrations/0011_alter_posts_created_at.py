# Generated by Django 5.0.4 on 2024-04-25 16:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0010_alter_posts_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]