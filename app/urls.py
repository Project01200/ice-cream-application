from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('signup/', views.HandleSignup, name='HandleSignup'),
    path('login/', views.HandleLogin, name='HandleLogin'),
    path('logout/', views.HandleLogout, name='HandleLogout'),
    path('ice-cream-selection/', views.ice_cream_selection, name='ice_cream_selection'),
    path('orders/', views.myorders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    # path('myorders/', views.myorders, name='myorders'),
    path('search/', views.search, name='search'),
    path('deleteOrder/<int:id>/', views.deleteOrder, name='deleteOrder'),
    path('toppings/', views.toppings, name='toppings'),
    path('containers/', views.containers, name='containers')
]
