from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order-history/', views.order_history, name='order_history'),
    path('mark-order-paid/<int:order_id>/', views.mark_order_as_paid, name='mark_order_as_paid'),
    path('sales-chart/', views.sales_chart, name='sales_chart'),
     path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
