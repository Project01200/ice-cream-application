from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from app.models import IceCreamFlavours, Toppings, MyOrders, Containers


def Home(request):
    myflav = IceCreamFlavours.objects.all()
    mytop = Toppings.objects.all()
    context = {"myflav": myflav, "mytop": mytop}
    return render(request, "home.html")


def HandleSignup(request):
    # logic
    if request.method == "POST":

        uname = request.POST.get("username")
        email = request.POST.get("email")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        phone = request.POST.get("phone")
        pass1 = request.POST.get("pass1")
        cpass = request.POST.get("pass2")
        # print(uname,email,fname,lname,pass1,cpass)

        # check whether user exists or not
        if (pass1 != cpass):
            messages.warning(request, "Password is'not Matching")
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
        myuser.phone = phone

        myuser.save()
        messages.success(request, "Signup Success")
        return redirect("/login")

    return render(request, "signup.html")


def HandleLogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        # print(email,pass1)
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


def ice_cream_selection(request):
    flavors = IceCreamFlavours.objects.all()
    context = {'flavors': flavors}
    return render(request, 'ice_cream_selection.html', context)


def toppings(request):
    mytop = Toppings.objects.all()
    context = {"mytop": mytop}
    return render(request, "toppings.html", context)

def containers(request):
    mycont = Containers.objects.all()
    context = {"mycont": mycont}
    return render(request, "containers.html", context)


def myorders(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login to place the Order....")
        return redirect("/login/")
    myflav = IceCreamFlavours.objects.all()
    mytop = Toppings.objects.all()

    # i am writing a logic to get the user details orders
    current_user = request.user.username

    # print(current_user)
    # i am fetching the data from table MyOrders based on emailid
    items = MyOrders.objects.filter(email=current_user)
    print(items)
    context = {"myflav": myflav, "mytop": mytop, "items": items}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        item = request.POST.get("items")
        quan = request.POST.get("quantity")
        phone = request.POST.get("num")
        print(name, email, item, quan, phone)

        price = ""
        for i in myflav:
            if item == i.name:
                price = i.price

            pass
        for i in mytop:
            if item == i.topping_name:
                price = i.topping_price

            pass

        newPrice = int(price) * int(quan)
        myquery = MyOrders(name=name, email=email, items=item, quantity=quan, price=newPrice,
                           phone_num=phone)
        myquery.save()
        messages.info(request, f"Order is Successful")
        return redirect("/orders")

    return render(request, "orders.html", context)


# def orders(request):
#     if not request.user.is_authenticated:
#         messages.warning(request,"Please Login to place the Order....")
#         return redirect("/login/")
#     myflav=IceCreamFlavours.objects.all()
#     mytop=Toppings.objects.all()
#
#     # i am writing a logic to get the user details orders
#     current_user=request.user.username
#
#     # print(current_user)
#     # i am fetching the data from table MyOrders based on emailid
#     items=Orders.objects.filter(email=current_user)
#     print(items)
#     context={"myflav":myflav,"mytop":mytop,"items":items}
#     if request.method =="POST":
#         name=request.POST.get("name")
#         email=request.POST.get("email")
#         item=request.POST.get("items")
#         quan=request.POST.get("quantity")
#         address=request.POST.get("address")
#         phone=request.POST.get("num")
#         print(name,email,item,quan,address,phone)
#
#         price=""
#         for i in myflav:
#             if item==i.name:
#                 price=i.price
#
#             pass
#         for i in mytop:
#             if item==i.prod_name:
#                 price=i.prod_price
#
#             pass
#
#         newPrice=int(price)*int(quan)
#         myquery=Orders(name=name, email=email, items=item, address=address, quantity=quan, price=newPrice, phone_num=phone)
#         myquery.save()
#         messages.info(request,f"Order is Successful")
#         return redirect("/orders")
#
#
#     return render(request,"orders.html",context)
# if not request.user.is_authenticated:
#     messages.warning(request, "Please Login to place the Order....")
#     return redirect("/login")
#
# if request.method == "POST":
#     name = request.POST.get("name")
#     email = request.POST.get("email")
#     item = request.POST.get("items")
#     quan = request.POST.get("quantity")
#     address = request.POST.get("address")
#     phone = request.POST.get("num")
#     price = request.POST.get("price")
#     try:
#         # Attempt to convert price and quantity to integers
#         price_int = int(price)
#         quan_int = int(quan)
#
#         # Calculate newPrice
#         newPrice = price_int * quan_int
#
#         myquery = MyOrders(name=name, email=email, items=item, address=address, quantity=quan, price=newPrice, phone_num=phone)
#         myquery.save()
#         messages.info(request, "Order is Successful")
#         return redirect("/orders")
#     except ValueError:
#         messages.error(request, "Invalid price or quantity. Please enter valid numbers.")
#         return redirect("/order_form")
# else:
#     return render(request, "orders.html")

def search(request):
    query = request.GET["getdata"]
    print(query)
    allPostsIceCreamFlavours = IceCreamFlavours.objects.filter(medicine_name__icontains=query)
    allPostsToppings = Toppings.objects.filter(prod_name__icontains=query)
    allPosts = allPostsIceCreamFlavours.union(allPostsToppings)

    return render(request, "search.html",
                  {"Med": allPostsIceCreamFlavours, "Prod": allPostsToppings, "allItems": allPosts})


def deleteOrder(request, id):
    print(id)
    query = MyOrders.objects.get(id=id)
    query.delete()
    messages.success(request, "Order Cancelled Successfully..")
    return redirect("/orders")


def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login to proceed to Checkout....")
        return redirect("/login/")

    current_user = request.user.username
    items = MyOrders.objects.filter(email=current_user)
    context = {"items": items}
    return render(request, "checkout.html", context)

# def myorders(request):
#     if not request.user.is_authenticated:
#         messages.warning(request, "Please Login to view your Orders....")
#         return redirect("/login")

#     current_user = request.user.username
#     items = MyOrders.objects.filter(email=current_user)
#     context = {"items": items}
#     return render(request, "myorders.html", context)


# def search(request):
#     query = request.GET["getdata"]
#     allPosts = MyOrders.objects.filter(items__icontains=query)
#     return render(request, "search.html", {"allItems": allPosts})


# def deleteOrder(request, id):
#     query = MyOrders.objects.get(id=id)
#     query.delete()
#     messages.success(request, "Order Cancelled Successfully..")
#     return redirect("/orders")
