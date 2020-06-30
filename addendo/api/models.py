from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Consultant(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
