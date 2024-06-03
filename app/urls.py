from app import views
from django.urls import path,include

urlpatterns = [
    path("",views.Home,name="Home"),
    path('signup',views.HandleSignup,name="HandleSignup"),
    path('login',views.HandleLogin,name="HandleLogin"),
    path('logout',views.HandleLogout,name="HandleLogout"),
    path("orders",views.orders,name="orders"),
    path("checkout",views.checkout,name="checkout"),
    path("search",views.search,name="search"),
    path("orders/<id>",views.deleteOrder,name="deleteOrder"),



]