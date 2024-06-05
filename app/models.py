from django.db import models

class IceCreamFlavours(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    desc=models.TextField()
    
class Toppings(models.Model):
    topping_name=models.CharField(max_length=20)
    topping_price=models.IntegerField()
    topping_desc=models.TextField()

class Containers(models.Model):
    car_name=models.CharField(max_length=20)
    car_price=models.IntegerField()

class Ingredients(models.Model):
    food_item=models.CharField(max_length=20)
    ingredients=models.CharField(max_length=500)

class Size(models.Model):
    scoop_size=models.IntegerField()
    Scoop_price=models.IntegerField()