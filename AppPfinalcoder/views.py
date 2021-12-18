#from django.core.checks.messages import ERROR
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from AppPfinalcoder.forms import CakesForm
from .models import Bakery, Cakes, Dessert
from .forms import CakesForm, DessertForm, BakeryForms

#login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView


# Create your views here.


def home(request):
    return render (request, 'AppPfinalcoder/home.html', {})
#___________________________________________________________________

# views Cakes

def cakes(request):
    cakes = None
    error = None
    if request.method == 'GET':
        order = request.GET.get('order', '')
        if order == '':
            cakes = Cakes.objects.all()
        try:
            order = int(order)
            cakes = Cakes.objects.filter(order=order)
        except:
            error = 'Enter a number.'
    return render (request, 'AppPfinalcoder/cakes.html', {'cakes':cakes, 'error': error})

#view create_cake

def create_cake(request):
    if request.method == 'POST':
        form = CakesForm(request.POST, request.FILES)
        
        if form.is_valid():
            dat_a = form.cleaned_data
            cakes = Cakes(order=dat_a['order'], fullname=dat_a['fullname'], address=dat_a['address'], phone=dat_a['phone'], email=dat_a['email'], product=dat_a['product'], units=dat_a['units'], imagen = dat_a['imagen'])
            cakes.save()
            return redirect('Cakes')
        
    
    form = CakesForm()
    return render(request, 'AppPfinalcoder/form_cakes.html', {'form': form})
    
#__________________________________________________________________________________________

#VIEW DESSERTS

def desserts(request):
    desserts = None
    error = None
    if request.method == 'GET':
        order = request.GET.get('order', '')
        if order == '':
            desserts = Dessert.objects.all()
        try:
            order = int(order)
            desserts = Dessert.objects.filter(order=order)
        except:
            error = 'Enter a number.'
    return render (request, 'AppPfinalcoder/desserts.html', {'desserts': desserts, 'error': error})


#view create_desserts
def create_desserts(request):
    if request.method == 'POST':
        form = DessertForm(request.POST, request.FILES)
        
        if form.is_valid():
            dat_a = form.cleaned_data
            desserts = Dessert(order=dat_a['order'], fullname=dat_a['fullname'], address=dat_a['address'], phone=dat_a['phone'], email=dat_a['email'], product=dat_a['product'], units=dat_a['units'], imagen = dat_a['imagen'])
            desserts.save()
            return redirect('Desserts')
        
    
    form = DessertForm()
    return render(request, 'AppPfinalcoder/form_desserts.html', {'form': form})

#_______________________________________________________________________________________________________________

#VIEW BAKERY

def bakery(request):
    bakery = None
    error = None
    if request.method == 'GET':
        order = request.GET.get('order', '')
        if order == '':
            bakery = Bakery.objects.all()
        try:
            order = int(order)
            bakery = Bakery.objects.filter(order=order)
        except:
            error = 'Enter a number.'
    return render (request, 'AppPfinalcoder/bakery.html', {'bakery': bakery, 'error': error})


#view create_bakery
def create_bakery(request):
    if request.method == 'POST':
        form = BakeryForms(request.POST, request.FILES)
        
        if form.is_valid():
            dat_a = form.cleaned_data
            bakery = Bakery(order=dat_a['order'], fullname=dat_a['fullname'], address=dat_a['address'], phone=dat_a['phone'], email=dat_a['email'], product=dat_a['product'], units=dat_a['units'], imagen = dat_a['imagen'])
            bakery.save()
            return redirect('Bakery')
        
    
    form = BakeryForms()
    return render(request, 'AppPfinalcoder/form_bakery.html', {'form': form})
#__________________________________________________________________________________________
#View login
def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return render(request, 'AppPfinalcoder/home.html', { 'message_register': True, 'message': f'Welcome to CAKES&BAKES {username}'})
            else:
                return render(request, 'AppPfinalcoder/login.html', {'form':form, 'message': 'User or password wrong', 'error': True})
        
        else:
           return render(request, 'AppPfinalcoder/login.html', {'form':form, 'message': 'Format wrong', 'error': True}) 
    
    
    form = AuthenticationForm()
    
    return render(request, 'AppPfinalcoder/login.html', {'form':form, 'message': '', 'error': False})

#_______________________________________________________________________________________________________________________________
#Register customer
def register_request(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            username=form.cleaned_data.get('username')
            
            form.save()
            
            return render(request, 'AppPfinalcoder/home.html', { 'message_register': True, 'message': f' User {username} created'})
    
    form = UserCreationForm()
    
    return render(request, 'AppPfinalcoder/register.html', {'form':form, 'message': '', 'error': False})

#________________________________________________________________________________________________________________
#PRICES
@login_required
def prices(request):
    return render(request, 'AppPfinalcoder/prices.html',{})

#_________________________________________________________________________________________________________________
#Imagen

class CakesDetailView(DetailView):
    model = Cakes
    template_name = "AppPfinalcoder/detailcake.html"
    
class DessertsDetailView(DetailView):
    model = Dessert
    template_name = "AppPfinalcoder/detaildessert.html"
    
class BakeryDetailView(DetailView):
    model = Bakery
    template_name = "AppPfinalcoder/detailbakery.html"
