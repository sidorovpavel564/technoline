from django.contrib import admin

from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'address', 'phone',
                    'email', 'created', 'updated')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'order', 'product',
                    'item_price', 'quantity', 'total')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
