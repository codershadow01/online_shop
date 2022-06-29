from django.contrib import admin
from .models import Product, Staff, Category, Cart, Customer, OrderPlaced

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'address', 'state', 'city', 'zipcode')

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity')

class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ('user', 'customer', 'items', 'ordered_date', 'ordered')

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Staff)
admin.site.register(Cart, CartAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(OrderPlaced, OrderPlacedAdmin)
