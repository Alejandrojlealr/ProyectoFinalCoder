from django.urls.conf import path
#import views
from .views import BakeryDetailView, DessertsDetailView, CakesDetailView, home, cakes, desserts, bakery, create_cake, create_desserts, create_bakery, login_request, prices, register_request, remove_cake, remove_desserts, remove_bakery, edit_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('', views.home, name='home')
    path('', home, name='home'),
    path('cakes/', cakes, name='Cakes' ),
    path('cakes/create/', create_cake, name='Create_cakes' ),
    path('cakes/create/<int:id>', create_cake, name='Create_cakes' ),
    path('cakes/remove/<int:id>', remove_cake, name='Remove_cakes' ),
    path('deserts/', desserts, name='Desserts'),
    path('desserts/create/' , create_desserts, name='Create_desserts' ),
    path('desserts/create/<int:id>', create_desserts, name='Create_desserts' ),
    path('desserts/remove/<int:id>', remove_desserts, name='Remove_desserts' ),
    path('bakery/', bakery, name='Bakery'),
    path('bakery/create/' , create_bakery, name='Create_bakery' ),
    path('bakery/create/<int:id>', create_bakery, name='Create_bakery' ),
    path('bakery/remove/<int:id>', remove_bakery, name='Remove_bakery' ),
    path('login/', login_request, name='Login'),
    path('register/', register_request, name='Register'),
    path('edit_user/', edit_user, name='Edit'),
    path('logout', LogoutView.as_view(template_name='AppPfinalcoder/logout.html'), name='Logout'),
    path('prices', prices, name='Prices'),
    path('cakes/<int:pk>/', CakesDetailView.as_view(),name='detailcake'),
    path('bakery/<int:pk>/', BakeryDetailView.as_view(),name='detailbakery'),
    path('desserts/<int:pk>/', DessertsDetailView.as_view(),name='detaildessert')
]


