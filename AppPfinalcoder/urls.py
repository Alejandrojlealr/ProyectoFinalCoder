from django.urls.conf import path
#import views
from .views import home, cakes, desserts, bakery, create_cake, create_desserts, create_bakery

urlpatterns = [
    #path('', views.home, name='home')
    path('', home, name='home'),
    path('cakes/', cakes, name='Cakes' ),
    path('cakes/create', create_cake, name='Create_cakes' ),
    path('deserts/', desserts, name='Desserts'),
    path('desserts/create', create_desserts, name='Create_desserts' ),
    path('bakery/', bakery, name='Bakery'),
    path('bakery/create', create_bakery, name='Create_bakery' )
]

