from django.contrib import admin
from .models import Product, Order, OrderItem, Category
from django.urls import reverse
from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'view_sales_chart')
    search_fields = ('name', 'description')
    
    def view_sales_chart(self, obj):
        url = reverse('sales_chart')
        return format_html('<a href="{}">Посмотреть график продаж</a>', url)

    view_sales_chart.short_description = 'График продаж'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total_price', 'is_paid')
    list_filter = ('is_paid', 'created_at')
    search_fields = ('user__username', 'id')
    ordering = ('-created_at',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('product__name',)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
