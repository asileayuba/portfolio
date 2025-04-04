# Generated by Django 5.1.7 on 2025-03-25 04:42

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0006_home"),
    ]

    operations = [
        migrations.AlterField(
            model_name="home",
            name="profile_image",
            field=cloudinary.models.CloudinaryField(
                max_length=255, verbose_name="image"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="profile_image",
            field=cloudinary.models.CloudinaryField(
                max_length=255, verbose_name="image"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True, verbose_name="image"
            ),
        ),
    ]
