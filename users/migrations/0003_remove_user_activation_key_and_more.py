# Generated by Django 4.2.6 on 2023-12-04 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_activation_key_user_activation_key_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='activation_key',
        ),
        migrations.RemoveField(
            model_name='user',
            name='activation_key_created',
        ),
    ]
