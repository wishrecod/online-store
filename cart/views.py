from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem
from products.models import Product, Order, OrderItem
from django.db.models import Sum
from .consumers import send_cart_update

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    send_cart_update(request.user)
    return redirect('cart_view')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    send_cart_update(request.user)
    return redirect('cart_view')

@login_required
def create_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        return redirect('cart_view')  # Если корзина пуста, перенаправляем обратно

    # Создаем заказ
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    order = Order.objects.create(user=request.user, total_price=total_price)

    # Переносим товары из корзины в заказ
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )
    cart_items.delete()  # Очищаем корзину

    return redirect('order_detail', order_id=order.id)
