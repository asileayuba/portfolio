# Generated by Django 5.1.7 on 2025-03-19 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0002_project"),
    ]

    operations = [
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "progress",
                    models.PositiveIntegerField(
                        help_text="Skill proficiency in percentage (1-100)"
                    ),
                ),
            ],
        ),
    ]
