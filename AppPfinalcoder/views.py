#from django.core.checks.messages import ERROR
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from AppPfinalcoder.forms import CakesForm
from .models import Bakery, Cakes, Dessert
from .forms import CakesForm, DessertForm, BakeryForms, RegisterUserForm, EditUserForm

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

def create_cake(request, id=0):
    id_cakes = 0
    try:
        cakes = Cakes.objects.get(id=id)
        id_cakes = cakes.id
    except Exception as e:
        cakes = None
        
    if request.method == 'POST':
        form = CakesForm(request.POST, request.FILES)
        
        if form.is_valid():
            dat_a = form.cleaned_data
            cakes = Cakes(order=dat_a['order'], fullname=dat_a['fullname'], address=dat_a['address'], phone=dat_a['phone'], email=dat_a['email'], product=dat_a['product'], units=dat_a['units'], imagen = dat_a['imagen'])
            cakes.save()
            return redirect('Cakes')
        
    elif cakes:
        form = CakesForm({'order':cakes.order, 'fullname': cakes.fullname, 'address':cakes.address, 'phone' : cakes.phone, 'email': cakes.email, 'product': cakes.product, 'units':cakes.units, 'imagen': cakes.imagen})
    else:
        #id_cakes = 0
        form = CakesForm()
    return render(request, 'AppPfinalcoder/form_cakes.html', {'form': form, 'id_cakes':id_cakes})

#view remove customer cakes

def remove_cake(request, id):
    cakes = Cakes.objects.get(id=id)
    cakes.delete()
    return render(request, 'AppPfinalcoder/remove_cakes.html', {'cakes': cakes})
    
    
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
def create_desserts(request, id=0):
    id_desserts = 0
    try:
        desserts = Dessert.objects.get(id=id)
        id_desserts = desserts.id
    except Exception as e:
        desserts = None
        
    if request.method == 'POST':
        form = DessertForm(request.POST, request.FILES)
        
        if form.is_valid():
            dat_a = form.cleaned_data
            desserts = Dessert(order=dat_a['order'], fullname=dat_a['fullname'], address=dat_a['address'], phone=dat_a['phone'], email=dat_a['email'], product=dat_a['product'], units=dat_a['units'], imagen = dat_a['imagen'])
            desserts.save()
            return redirect('Desserts')
        
    elif desserts:
        form = DessertForm({'order':desserts.order, 'fullname': desserts.fullname, 'address':desserts.address, 'phone' : desserts.phone, 'email': desserts.email, 'product': desserts.product, 'units':desserts.units, 'imagen': desserts.imagen})
    else:
        form = DessertForm()
    return render(request, 'AppPfinalcoder/form_desserts.html', {'form': form, 'id_desserts': id_desserts})

#View remove desserts
def remove_desserts(request, id):
    desserts = Dessert.objects.get(id=id)
    desserts.delete()
    return render(request, 'AppPfinalcoder/remove_desserts.html', {'desserts': desserts})

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
def create_bakery(request, id=0):
    id_bakery = 0
    try:
        bakery =Bakery.objects.get(id=id)
        id_bakery = bakery.id
    except Exception as e:
        bakery = None
        
    if request.method == 'POST':
        form = BakeryForms(request.POST, request.FILES)
        
        if form.is_valid():
            dat_a = form.cleaned_data
            bakery = Bakery(order=dat_a['order'], fullname=dat_a['fullname'], address=dat_a['address'], phone=dat_a['phone'], email=dat_a['email'], product=dat_a['product'], units=dat_a['units'], imagen = dat_a['imagen'])
            bakery.save()
            return redirect('Bakery')
        
    elif bakery:
        form = BakeryForms({'order':bakery.order, 'fullname': bakery.fullname, 'address':bakery.address, 'phone' : bakery.phone, 'email': bakery.email, 'product': bakery.product, 'units': bakery.units, 'imagen': bakery.imagen})
    else:
        form = BakeryForms()
    return render(request, 'AppPfinalcoder/form_bakery.html', {'form': form, 'id_bakery': id_bakery})

#View remove bakery
def remove_bakery(request, id):
    bakery = Bakery.objects.get(id=id)
    bakery.delete()
    return render(request, 'AppPfinalcoder/remove_bakery.html', {'bakery': bakery})
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
        form = RegisterUserForm(request.POST)
        
        if form.is_valid():
            username=form.cleaned_data.get('username')
            
            form.save()
            
            return render(request, 'AppPfinalcoder/home.html', { 'message_register': True, 'message': f' User {username} created'})
    
    form = RegisterUserForm()
    
    return render(request, 'AppPfinalcoder/register.html', {'form':form, 'message': '', 'error': False})

#______________________________________________________________________________________________________________________________________
#Edit User
@login_required
def edit_user(request):
    user = request.user
    
    if request.method == 'POST':
        form = EditUserForm(request.POST)
        
        if form.is_valid():
            
            data = form.cleaned_data
            
            
            user.email = data['email']
            user.password1 = data['password1']
            user.password2 = data['password2']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            
            user.save()
            
            
            return render(request, 'AppPfinalcoder/home.html', { 'message_editer': True, 'message': f' User edited'})
    else:
        form = EditUserForm(initial= {'first_name': user.first_name, 'last_name': user.last_name , 'email': user.email})
    
    return render(request, 'AppPfinalcoder/edit_user.html', {'form':form, 'message': '', 'error': False})

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
