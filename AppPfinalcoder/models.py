from django.db import models

# Create your models here.
class Cakes(models.Model):
    fullname=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    product=models.CharField(max_length=30)
    units=models.IntegerField()
    
class Dessert(models.Model):
    fullname=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    product=models.CharField(max_length=30)
    units=models.IntegerField()
    
class Bakery(models.Model):
    fullname=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    product=models.CharField(max_length=30)
    units=models.IntegerField()
    
    
    
    