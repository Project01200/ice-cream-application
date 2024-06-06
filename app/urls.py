from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('signup/', views.HandleSignup, name='HandleSignup'),
    path('login/', views.HandleLogin, name='HandleLogin'),
    path('logout/', views.HandleLogout, name='HandleLogout'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('myorders/', views.myorders, name='myorders'),
    path('search/', views.search, name='search'),
    path('deleteOrder/<int:id>/', views.deleteOrder, name='deleteOrder'),
]
