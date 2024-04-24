from django.db import models

# Create your models here.

class testmodel(models.Model):
    modelname=models.CharField(max_length=180)
    modelage=models.CharField(max_length=180)