from django.contrib import admin
from .models import IceCreamFlavours, MyOrders,Toppings,Containers,Size,Ingredients

admin.site.register(IceCreamFlavours)
admin.site.register(Toppings)
admin.site.register(Containers)
admin.site.register(Size)
admin.site.register(Ingredients)
admin.site.register(MyOrders)