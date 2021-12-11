from django.contrib import admin

from .models import Bakery, Cakes, Dessert

# Register your models here.

admin.site.register(Cakes)
admin.site.register(Dessert)
admin.site.register(Bakery)

