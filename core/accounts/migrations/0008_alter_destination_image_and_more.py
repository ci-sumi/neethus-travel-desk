# Generated by Django 5.1 on 2024-11-04 18:34

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]