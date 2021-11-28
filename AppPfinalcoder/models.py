from django.db import models

# Create your models here.
class Cakes(models.Model):
    order=models.IntegerField(default=0)
    fullname=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    product=models.CharField(max_length=30)
    units=models.IntegerField()
    
    def __str__(self):
      return f'Customer order {self.order}'
    
class Dessert(models.Model):
    order=models.IntegerField(default=0)
    fullname=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    product=models.CharField(max_length=30)
    units=models.IntegerField()
    
    def __str__(self):
       return f'Customer order {self.order}'
    
class Bakery(models.Model):
    order=models.IntegerField(default=0)
    fullname=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    product=models.CharField(max_length=30)
    units=models.IntegerField()
    
    def __str__(self):
       return f'Customer order {self.order}'
    
    
    
    