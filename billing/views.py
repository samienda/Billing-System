from rest_framework.viewsets import ModelViewSet

from .serializers import CustomerSerializer, ProductSerializer, TransactionSerializer
from .models import Customer, Product, Transaction


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
