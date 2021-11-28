from django.urls.conf import path
#import views
from .views import home, cakes, desserts, bakery, create_cake

urlpatterns = [
    #path('', views.home, name='home')
    path('', home, name='home'),
    path('cakes/', cakes, name='Cakes' ),
    path('cakes/create', create_cake, name='Create_cakes' ),
    path('deserts/', desserts, name='Desserts'),
    path('bakery/', bakery, name='Bakery')
]

