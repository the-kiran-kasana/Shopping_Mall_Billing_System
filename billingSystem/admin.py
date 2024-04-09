from django.contrib import admin
from .models import Bill, BillProduct, Customer, Product

admin.site.register([Bill, BillProduct, Customer, Product])

