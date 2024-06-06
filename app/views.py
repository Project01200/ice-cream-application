import re
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from app.models import MyOrders


def Home(request):
    return render(request, "home.html")


def HandleSignup(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        pass1 = request.POST.get("pass1")
        cpass = request.POST.get("pass2")

        if pass1 != cpass:
            messages.warning(request, "Password isn't matching")
            return redirect("/signup")

        try:
            if User.objects.get(username=email):
                messages.info(request, "Username is taken..")
                return redirect("/signup")
        except:
            pass

        myuser = User.objects.create_user(email, uname, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Signup Success")
        return redirect("/login")

    return render(request, "signup.html")


def HandleLogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        myuser = authenticate(username=email, password=pass1)

        if myuser is not None:
            login(request, myuser)
            messages.info(request, "Login Successful")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("/login")

    return render(request, "login.html")


def HandleLogout(request):
    logout(request)
    messages.warning(request, "Logout")
    return redirect("/login")


def orders(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login to place the Order....")
        return redirect("/login")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        item = request.POST.get("items")
        quan = request.POST.get("quantity")
        address = request.POST.get("address")
        phone = request.POST.get("num")
        price = request.POST.get("price")
        newPrice = int(price) * int(quan)
        myquery = MyOrders(name=name, email=email, items=item, address=address, quantity=quan, price=newPrice, phone_num=phone)
        myquery.save()
        messages.info(request, "Order is Successful")
        return redirect("/orders")

    return render(request, "orders.html")


def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login to proceed to Checkout....")
        return redirect("/login")

    current_user = request.user.username
    items = MyOrders.objects.filter(email=current_user)
    context = {"items": items}
    return render(request, "checkout.html", context)


def myorders(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login to view your Orders....")
        return redirect("/login")

    current_user = request.user.username
    items = MyOrders.objects.filter(email=current_user)
    context = {"items": items}
    return render(request, "myorders.html", context)


def search(request):
    query = request.GET["getdata"]
    allPosts = MyOrders.objects.filter(items__icontains=query)
    return render(request, "search.html", {"allItems": allPosts})


def deleteOrder(request, id):
    query = MyOrders.objects.get(id=id)
    query.delete()
    messages.success(request, "Order Cancelled Successfully..")
    return redirect("/orders")
