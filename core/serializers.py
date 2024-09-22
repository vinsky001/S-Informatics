from rest_framework import serializers
from .models import Customer, Order
from phonenumber_field.serializerfields import PhoneNumberField

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['code', 'name', 'email', 'phone_number']

    def validate_phone_number(self, value):
        if not value:
            raise serializers.ValidationError("Phone number is required.")
        return value

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'order_date', 'amount', 'time', 'item']
        read_only_fields = ['time']