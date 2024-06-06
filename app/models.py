from django.db import models

class MyOrders(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    items = models.CharField(max_length=255)
    address = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    phone_num = models.CharField(max_length=15)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.name}"

class IceCreamFlavours(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    desc = models.TextField()

    def __str__(self):
        return self.name
    
class Toppings(models.Model):
    topping_name = models.CharField(max_length=20)
    topping_price = models.IntegerField()
    topping_desc = models.TextField()

    def __str__(self):
        return self.topping_name

class Containers(models.Model):
    container_name = models.CharField(max_length=20)
    container_price = models.IntegerField()

    def __str__(self):
        return self.container_name

class Ingredients(models.Model):
    food_item = models.CharField(max_length=20)
    ingredients = models.CharField(max_length=500)

    def __str__(self):
        return self.food_item

class Size(models.Model):
    scoop_size = models.IntegerField()
    scoop_price = models.IntegerField()

    def __str__(self):
        return f"{self.scoop_size} scoops"
