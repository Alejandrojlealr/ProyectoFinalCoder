#from typing_extensions import Required
#from datetime import datetime
from django import forms

class CakesForm(forms.Form):
    date=forms.DateTimeField()
    order=forms.IntegerField(required=True)
    fullname=forms.CharField(max_length=30)
    address=forms.CharField(max_length=50)
    phone=forms.IntegerField()
    email=forms.EmailField()
    product=forms.CharField(max_length=30)
    units=forms.IntegerField()
    
class DessertForm(forms.Form):
    date=forms.DateTimeField()
    order=forms.IntegerField(required=True)
    fullname=forms.CharField(max_length=30)
    address=forms.CharField(max_length=50)
    phone=forms.IntegerField()
    email=forms.EmailField()
    product=forms.CharField(max_length=30)
    units=forms.IntegerField()
    
class BakeryForms(forms.Form):
    date=forms.DateTimeField()
    order=forms.IntegerField(required=True)
    fullname=forms.CharField(max_length=30)
    address=forms.CharField(max_length=50)
    phone=forms.IntegerField()
    email=forms.EmailField()
    product=forms.CharField(max_length=30)
    units=forms.IntegerField()
    