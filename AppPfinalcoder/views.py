#from django.core.checks.messages import ERROR
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from AppPfinalcoder.forms import CakesForm
from .models import Bakery, Cakes, Dessert
from .forms import CakesForm

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
        form = CakesForm(request.POST)
        
        if form.is_valid():
            dat_a = form.cleaned_data
            cakes = Cakes(order=dat_a['order'], fullname=dat_a['fullname'], address=dat_a['address'], phone=dat_a['phone'], email=dat_a['email'], product=dat_a['product'], units=dat_a['units'])
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
