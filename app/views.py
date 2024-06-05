import re

from django.shortcuts import render
from .models import IceCreamFlavours, Containers, Toppings

def ice_cream_shop(request):
  ice_creams = IceCreamFlavours.objects.all()
  containers = Containers.objects.all()
  toppings = Toppings.objects.all()
  size = Size.objects.all()
  context = {'ice_creams': ice_creams, 'containers': containers, 'toppings': toppings, 'size':size}
  return render(request, 'ice_cream_shop.html', context)