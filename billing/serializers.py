from rest_framework import serializers
from djoser.serializers import UserSerializer as BaseUserSerializer
from .models import Customer, Product, Transaction


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class CustomerSerializer(serializers.ModelSerializer):
    total_billed_amount = serializers.ReadOnlyField()
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'total_billed_amount']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'productname', 'price', 'stock']


class TransactionSerializer(serializers.ModelSerializer):
    total_amount = serializers.ReadOnlyField()
    employee = UserSerializer(read_only=True)
    class Meta:
        model = Transaction
        fields = ['id', 'customer', 'product',
                  'quantity', 'total_amount', 'timestamp', 'employee']

    def create(self, validated_data):
        product = validated_data['product']
        quantity = validated_data['quantity']
        validated_data['total_amount'] = product.price * quantity
        return super().create(validated_data)
