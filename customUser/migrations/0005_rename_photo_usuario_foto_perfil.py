# Generated by Django 5.0.4 on 2024-04-24 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0004_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='photo',
            new_name='foto_perfil',
        ),
    ]
