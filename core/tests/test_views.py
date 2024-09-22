from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Customer, Order
from unittest.mock import patch
from phonenumber_field.phonenumber import PhoneNumber

class CustomerViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_upload_customers(self):
        data = [
            {'name': 'John Doe', 'email': 'john@example.com', 'phone_number': '+12345678901'},
            {'name': 'Jane Doe', 'email': 'jane@example.com', 'phone_number': '+12345678902'}
        ]
        response = self.client.post('/api/customers/upload_customers/', data, format='json')
        print("Response content:", response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)
        
class OrderViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.customer = Customer.objects.create(
            name='Test Customer',
            email='test@example.com',
            phone_number=PhoneNumber.from_string('+1234567890')
        )

    def test_upload_orders(self):
        data = [
            {'customer': str(self.customer.code), 'item': 'Item 1', 'amount': 10.99, 'order_date': '2023-05-01'},
            {'customer': str(self.customer.code), 'item': 'Item 2', 'amount': 20.99, 'order_date': '2023-05-02'}
        ]
        response = self.client.post('/api/orders/upload_orders/', data, format='json')
        print("Response content:", response.content) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)

    @patch('core.views.send_sms')
    def test_perform_create(self, mock_send_sms):
        data = {'customer': str(self.customer.code), 'item': 'Test Item', 'amount': 15.99, 'order_date': '2023-05-03'}
        response = self.client.post('/api/orders/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        mock_send_sms.assert_called_once_with(self.customer.phone_number, 'New order placed: Test Item for $15.99')