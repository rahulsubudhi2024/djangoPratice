from django.db import models
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    instructor = models.CharField(max_length=30)
    rating = models.FloatField()

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})