from django.contrib import admin

# Register your models here.
from .models import Order, OrderTag


admin.site.register(Order)
admin.site.register(OrderTag)
