# Generated by Django 5.1.4 on 2025-01-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("name", models.CharField(max_length=30)),
                ("description", models.CharField(max_length=30)),
                ("instructor", models.CharField(max_length=30)),
                ("rating", models.FloatField()),
            ],
        ),
    ]
