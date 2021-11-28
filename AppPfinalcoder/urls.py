from django.urls.conf import path
#import views
from .views import home

urlpatterns = [
    #path('', views.home, name='home')
    path('', home, name='home')
]

