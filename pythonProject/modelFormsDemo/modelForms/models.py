from django.db import models

# Create your models here.

class Project(models.Model):
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=30)
    assignedTo = models.CharField(max_length=20)
    priority = models.IntegerField(blank=True, null=True)
