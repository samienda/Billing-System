from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=50, default='a')
    last_name = models.CharField(max_length=50, default='a')
    total_billed_amount = models.DecimalField(validators=[MinValueValidator(0.0)],
                                              max_digits=10, decimal_places=2, default=0.0)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    productname = models.CharField(max_length=50)
    price = models.DecimalField(validators=[MinValueValidator(
        1.0)], decimal_places=2, max_digits=10)
    stock = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.productname}"


class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=0)
    total_amount = models.DecimalField(
        validators=[MinValueValidator(1.0)], decimal_places=2, max_digits=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        product = self.product
        customer = self.customer

        if self.quantity > product.stock:
            return False

        product.stock -= self.quantity
        # print(self.total_amount)
        # print(customer.total_billed_amount)
        customer.total_billed_amount += self.total_amount if self.total_amount else -1
        # print(customer.total_billed_amount)

        product.save()
        customer.save()

        super().save(*args, **kwargs)
