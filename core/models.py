from django.db import models
import uuid
from datetime import date
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField



class Customer(models.Model):
    name = models.CharField(max_length=100)
    code = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )  # uniqueIdentifier
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(max_length=15, unique=True)
    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    item = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
