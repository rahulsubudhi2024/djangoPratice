from django.db import models

# Create your models here.

class Employee(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    salary=models.FloatField()
    email=models.CharField(max_length=35)

class Programer(models.Model):
    name=models.CharField(max_length=30)
    sal=models.IntegerField()

class Project(models.Model):
    name=models.CharField(max_length=30)
    programers=models.ManyToManyField(Programer)

class Customer(models.Model):
    name=models.CharField(max_length=30)

class PhoneNumber(models.Model):
    type=models.CharField(max_length=10)
    number=models.CharField(max_length=10)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

class Person(models.Model):
    firstName=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    age=models.IntegerField()

class License(models.Model):
    type=models.CharField(max_length=30)
    validFrom=models.DateField()
    validTo=models.DateField()
    person=models.OneToOneField(Person,on_delete=models.CASCADE)