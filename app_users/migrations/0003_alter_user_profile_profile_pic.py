# Generated by Django 3.2.5 on 2021-08-19 19:24

import app_users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_auto_20210819_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=app_users.models.path_and_rename, verbose_name='Profile Picture'),
        ),
    ]
