# Generated by Django 5.0.4 on 2024-04-25 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='color_icon',
            field=models.CharField(default='none', max_length=10),
        ),
    ]
