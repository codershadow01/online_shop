from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.hpage, name="homepage"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path("add-to-cart/", views.cart, name="cart"),
    path('cart/', views.cartshow, name="show_cart"),
    path("place-order/", views.placeorder, name="place_order"),
    path("payment-done/", views.paymentdone, name="paymentdone"),
    path("orders/", views.orders, name="orders"),
    path("viewprofile/", views.profile, name="profile"),
    path("address/", views.adress, name="address"),
    path('<slug:category>/', views.category, name="category"),
    path('<slug:category>/<slug:slug>/', views.product, name="product")
]
