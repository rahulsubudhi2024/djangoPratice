# Generated by Django 5.1.4 on 2024-12-20 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modelForms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="endDate",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="priority",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="startDate",
            field=models.DateField(blank=True, null=True),
        ),
    ]