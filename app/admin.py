from django.contrib import admin
from .models import IceCreamFlavour,Toppings,Container,Size,Ingredients

admin.site.register(IceCreamFlavour)
admin.site.register(Toppings)
admin.site.register(Container)
admin.site.register(Size)
admin.site.register(Ingredients)