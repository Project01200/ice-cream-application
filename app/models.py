

from django.db import models

class IceCreamFlavours(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(upload_to="flavors", blank=True, null=True)

    def __str__(self):
        return self.name


class Toppings(models.Model):
    topping_name = models.CharField(max_length=20, unique=True)
    topping_price = models.IntegerField()
    topping_image = models.ImageField(upload_to="toppings", blank=True, null=True)

    def __str__(self):
        return self.topping_name


class Containers(models.Model):
    container_name = models.CharField(max_length=20)
    container_price = models.IntegerField()
    container_image = models.ImageField(upload_to="containers", blank=True, null=True)

    def __str__(self):
        return self.container_name

class MyOrders(models.Model):
    name = models.CharField(max_length=50)
    flavor = models.ForeignKey(IceCreamFlavours, on_delete=models.CASCADE)
    topping = models.ForeignKey(Toppings, on_delete=models.CASCADE)
    container = models.ForeignKey(Containers, on_delete=models.CASCADE)
    email = models.EmailField()
    items = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.pk} by {self.name}"

class Containers_Ingredients(models.Model):
    container = models.ForeignKey(Containers, on_delete=models.CASCADE)
    container_ingredients = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return self.container_ingredients

class Toppings_Ingredients(models.Model):
    topping = models.ForeignKey(Toppings, on_delete=models.CASCADE)
    topping_ingredients = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return self.topping_ingredients

class Flavors_Ingredients(models.Model):
    flavor = models.ForeignKey(IceCreamFlavours, on_delete=models.CASCADE)
    flavor_ingredients = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return self.flavor_ingredients

# class Orders(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#     items = models.CharField(max_length=255)
#     address = models.TextField()
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     phone_num = models.CharField(max_length=15)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Order {self.id} by {self.name}"




# class Ingredients(models.Model):
#     flavour = models.ForeignKey(IceCreamFlavours, on_delete=models.CASCADE)
#     flavour_ingredients = models.TextField()
#
#     container = models.ForeignKey(Containers, on_delete=models.CASCADE)
#     container_ingredients = models.TextField()
#
#     toppings = models.ForeignKey(Toppings, on_delete=models.CASCADE)
#     toppings_ingredients = models.TextField()
#
#     def __str__(self):
#         return f"Ingredients for {self.flavour}"


class Size(models.Model):
    scoop_size = models.IntegerField()
    scoop_price = models.IntegerField()

    def __str__(self):
        return f"{self.scoop_size} scoops"

# class Orders(models.Model):
#     name=models.CharField(max_length=30)
#     email=models.EmailField()
#     items=models.CharField(max_length=1500)
#     quantity=models.CharField(max_length=100)
#     price=models.CharField(max_length=100)
#     phone_num=models.CharField(max_length=10)
#
#     def __int__(self):
#         return self.id
