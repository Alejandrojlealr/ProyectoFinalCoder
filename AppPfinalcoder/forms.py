#from typing_extensions import Required
#from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import fields

class CakesForm(forms.Form):
    date=forms.DateTimeField()
    order=forms.IntegerField(required=True)
    fullname=forms.CharField(max_length=30)
    address=forms.CharField(max_length=50)
    phone=forms.IntegerField()
    email=forms.EmailField()
    product=forms.CharField(max_length=30)
    units=forms.IntegerField()
    imagen = forms.ImageField()
    
class DessertForm(forms.Form):
    date=forms.DateTimeField()
    order=forms.IntegerField(required=True)
    fullname=forms.CharField(max_length=30)
    address=forms.CharField(max_length=50)
    phone=forms.IntegerField()
    email=forms.EmailField()
    product=forms.CharField(max_length=30)
    units=forms.IntegerField()
    imagen = forms.ImageField()
    
class BakeryForms(forms.Form):
    date=forms.DateTimeField()
    order=forms.IntegerField(required=True)
    fullname=forms.CharField(max_length=30)
    address=forms.CharField(max_length=50)
    phone=forms.IntegerField()
    email=forms.EmailField()
    product=forms.CharField(max_length=30)
    units=forms.IntegerField()
    imagen = forms.ImageField()
    
    
class RegisterUserForm(UserCreationForm):
    #username = forms.CharField(label='User', max_length=30)
    first_name = forms.CharField(label = 'First name')
    last_name = forms.CharField(label = 'Last name')
    email = forms.EmailField(label = 'Email')
    password1 = forms.CharField(label = 'Password', widget= forms.PasswordInput)
    password2 = forms.CharField(label = 'Repeat password', widget= forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2' ]
        help_texts = {k: '' for k in fields}
        
        
class EditUserForm(UserCreationForm):
    #username = forms.CharField(label='User', max_length=30)
    email = forms.EmailField(label = 'Edit Email')
    password1 = forms.CharField(label = 'Password', widget= forms.PasswordInput)
    password2 = forms.CharField(label = 'Repeat password', widget= forms.PasswordInput)
    first_name = forms.CharField(label = 'First name')
    last_name = forms.CharField(label = 'Last name')
    
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'password1', 'password2', ]
        help_texts = {k: '' for k in fields}