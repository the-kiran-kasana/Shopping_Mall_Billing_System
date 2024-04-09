from rest_framework import serializers
from .models import Product, Customer, Bill, BillProduct
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Bill
        fields = ['id', 'date', 'total_amount', 'status', 'customer', 'employee']
        read_only_fields = ('date', 'employee',) 


class BillProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillProduct
        fields = '__all__'
