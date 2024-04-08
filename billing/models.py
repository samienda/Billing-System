from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Employee(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()


class Product(models.Model):
    productname = models.CharField(max_length=50)
    price = models.DecimalField(MinValueValidator(
        1.0), decimal_places=2, max_digits=10)
    stock = models.PositiveBigIntegerField(default=0)


class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=0)
    total_amount = models.DecimalField(
        MinValueValidator(1.0), decimal_places=2, max_digits=10)
    timestamp = models.DateTimeField(auto_now_add=True)
