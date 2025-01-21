# Generated by Django 5.1.4 on 2025-01-21 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("lastName", models.CharField(max_length=20)),
                ("firstName", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="ClinicalData",
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
                ("componentName", models.CharField(max_length=20)),
                ("componentValue", models.CharField(max_length=20)),
                ("measureDateTime", models.DateTimeField(auto_now_add=True)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clinicalsApp.patient",
                    ),
                ),
            ],
        ),
    ]
