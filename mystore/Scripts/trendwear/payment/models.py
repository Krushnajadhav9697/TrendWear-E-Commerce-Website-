from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    delivery_street = models.CharField(max_length=255)
    delivery_city = models.CharField(max_length=100)
    delivery_state = models.CharField(max_length=100)
    delivery_pin_code = models.CharField(max_length=10)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=50, default='Pending')
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f'Order {self.id} by {self.user.username}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f'{self.quantity} x {self.product.name} i'

class PayPalTransaction(models.Model):
    order = models.ForeignKey('order', on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255, unique=True)
    payer_email = models.EmailField()
    payment_status = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.transaction_id} - {self.payment_status}"