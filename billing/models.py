from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings
# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(sett)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
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
