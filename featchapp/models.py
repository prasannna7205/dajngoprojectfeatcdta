from django.db import models

# Create your models here.
class employees(models.Model):
    name = models.CharField(max_length=100)
    eno=models.IntegerField()
    esal=models.IntegerField()
    addrs=models.CharField(max_length=100)
