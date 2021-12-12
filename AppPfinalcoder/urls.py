from django.urls.conf import path
#import views
from .views import home, cakes, desserts, bakery, create_cake, create_desserts, create_bakery, login_request, prices, register_request
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('', views.home, name='home')
    path('', home, name='home'),
    path('cakes/', cakes, name='Cakes' ),
    path('cakes/create', create_cake, name='Create_cakes' ),
    path('deserts/', desserts, name='Desserts'),
    path('desserts/create', create_desserts, name='Create_desserts' ),
    path('bakery/', bakery, name='Bakery'),
    path('bakery/create', create_bakery, name='Create_bakery' ),
    path('login/', login_request, name='Login'),
    path('register/', register_request, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppPfinalcoder/logout.html'), name='Logout'),
    path('prices', prices, name='Prices'),
]


