from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=30)
    releaseDate = models.DateField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)