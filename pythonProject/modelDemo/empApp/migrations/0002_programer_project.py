# Generated by Django 5.1.4 on 2025-01-21 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Programer",
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
                ("sal", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("programers", models.ManyToManyField(to="empApp.programer")),
            ],
        ),
    ]
