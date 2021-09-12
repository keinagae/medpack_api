
from django.contrib import admin

from .models import Order, OrderItem




class OrderItemAdmin(admin.TabularInline):
    list_display = ('id', 'order', 'quantity', 'product')
    list_filter = ('order', 'product')
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status','address','phone', 'created_at')
    list_filter = ('user', 'created_at','status')
    date_hierarchy = 'created_at'
    inlines = [
        OrderItemAdmin
    ]

    @admin.display(description='User Address')
    def address(self, obj):
        return obj.user.profile.address

    @admin.display(description='User Phone')
    def phone(self, obj):
        return obj.user.profile.phone

