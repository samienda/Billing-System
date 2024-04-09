from rest_framework import serializers
from djoser.serializers import UserSerializer as BaseUserSerializer
from .models import Customer, Product, Transaction


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'firstname', 'lastname']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'total_billed_amount']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'productname', 'price', 'stock']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'customer', 'product',
                  'quantity', 'total_amount', 'timestamp', 'employee']
