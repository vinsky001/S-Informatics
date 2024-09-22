# S-Informatics

S-Informatics is a Django-based web service that manages customer information and orders. It provides a REST API for inputting and uploading customer and order data, with OpenID Connect authentication and SMS notifications for new orders.

## Features

- Simple customer and order database
- REST API for customer and order management
- Bulk upload functionality for customers and orders
- Authentication and authorization via OpenID Connect
- SMS notifications for new orders using Africa's Talking SMS gateway
- Comprehensive unit tests with coverage checking
- CI/CD pipeline for automated deployment

## Technology Stack

- Python 3.x
- Django 3.x
- Django Rest Framework
- PostgreSQL
- OpenID Connect for authentication
- Africa's Talking SMS gateway for notifications
- GitHub Actions for CI/CD

## Database Design

### Customers
- name (string)
- code (UUID, primary key)

### Orders
- customer (foreign key to Customers)
- item (string)
- amount (decimal)
- time (datetime)

## API Endpoints

- `/api/customers/`: List and create customers
- `/api/customers/upload/`: Bulk upload customers
- `/api/orders/`: List and create orders
- `/api/orders/upload/`: Bulk upload orders

## Authentication

This project uses OpenID Connect for authentication. You need to set up an OpenID Connect provider and configure the client in the Django settings.

## SMS Notifications

When an order is added, an SMS is sent to the customer using the Africa's Talking SMS gateway. The sandbox environment is used for development and testing.

## Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/S-Informatics.git
   cd S-Informatics
   ```

2. Set up a virtual environment and install dependencies:
   ```
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Configure environment variables for OpenID Connect and Africa's Talking SMS gateway.

5. Run the development server:
   ```
   python manage.py runserver
   ```

## Testing

Run the tests and generate a coverage report:
```
python manage.py test
```
