from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product, Customer, Bill, BillProduct
from .serializer import ProductSerializer, CustomerSerializer, BillSerializer, BillProductSerializer, UserSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Sum
from rest_framework.views import APIView

# User Serializer
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Product Views
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

# Customer Views
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

# Bill Views
class BillList(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)

class BillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]

# BillProduct Views
class BillProductList(generics.ListCreateAPIView):
    queryset = BillProduct.objects.all()
    serializer_class = BillProductSerializer
    permission_classes = [IsAuthenticated]

class BillProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillProduct.objects.all()
    serializer_class = BillProductSerializer
    permission_classes = [IsAuthenticated]

class TopSellingEmployee(APIView):

    def get(self, request, format=None):
        top_employee = Bill.objects.values('employee__id', 'employee__username') \
            .annotate(total_sales=Sum('total_amount')) \
            .order_by('-total_sales') \
            .first()
        
        if top_employee:
            employee_details = {
                'employee_id': top_employee['employee__id'],
                'username': top_employee['employee__username'],
                'total_sales': top_employee['total_sales'],
            }
            return JsonResponse(employee_details)
        else:
            return JsonResponse({'message': 'No sales data found'}, status=404)
