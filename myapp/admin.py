from django.contrib import admin

# Register your models here.
from .models import *


class AdminOrderApp(admin.ModelAdmin):
    list_display = ('customer', 'product', 'price', 'counter', 'price_all', 'create_at', 'update_at')


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OrderApp, AdminOrderApp)
