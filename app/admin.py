from django.contrib import admin
from .models import IceCreamFlavours, Toppings, Containers, Size, MyOrders, Toppings_Ingredients, Flavors_Ingredients, \
    Containers_Ingredients

admin.site.register(IceCreamFlavours)
admin.site.register(Toppings)
admin.site.register(Containers)
admin.site.register(Size)
admin.site.register(Flavors_Ingredients)
admin.site.register(Toppings_Ingredients)
admin.site.register(Containers_Ingredients)
admin.site.register(MyOrders)