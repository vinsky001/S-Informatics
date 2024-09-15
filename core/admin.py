from django.contrib import admin
from .models import Customer, Order

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'code')    
    search_fields = ('name', 'code')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'amount', 'time')
    
    list_filter = ('order_date', 'customer')
    search_fields = ('customer__name', 'customer__code')