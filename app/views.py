import re

from django.shortcuts import render
from .models import IceCreamFlavor, Container, Topping

def ice_cream_shop(request):
  ice_creams = IceCreamFlavor.objects.all()
  containers = Container.objects.all()
  toppings = Topping.objects.all()
  size = Size.objects.all()
  context = {'ice_creams': ice_creams, 'containers': containers, 'toppings': toppings, 'size':size}
  return render(request, 'ice_cream_shop.html', context)