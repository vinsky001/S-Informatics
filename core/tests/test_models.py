from django.test import TestCase
from core.models import Customer, Order

class CustomerModelTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name='Test Customer',
            email='test@example.com',
            phone_number='+1234567890'
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, 'Test Customer')
        self.assertEqual(self.customer.email, 'test@example.com')
        self.assertEqual(self.customer.phone_number, '+1234567890')

class OrderModelTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name='Test Customer',
            email='test@example.com',
            phone_number='+1234567890'
        )
        self.order = Order.objects.create(
            customer=self.customer,
            item='Test Item',
            amount=15.99
        )

    def test_order_creation(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.item, 'Test Item')
        self.assertEqual(self.order.amount, 15.99)
        self.assertIsNotNone(self.order.order_date)