from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order, OrderItem, Category
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q, Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.http import HttpResponse

def product_list(request):
    query = request.GET.get('q', '')  # Поисковой запрос
    category_id = request.GET.get('category', None)  # Фильтрация по категории

    # Фильтруем товары
    products = Product.objects.all()
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if category_id:
        products = products.filter(category_id=category_id)

    # Пагинация
    products = products.order_by('id')
    paginator = Paginator(products, 5)  # 5 товаров на страницу
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    categories = Category.objects.all()  # Для отображения списка категорий

    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'query': query,
        'page': page,
    })

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'products/order_detail.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'products/order_history.html', {'orders': orders})

@staff_member_required
def mark_order_as_paid(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.is_paid = True
    order.save()
    return redirect('order_detail', order_id=order.id)



def sales_chart(request):
    if not request.user.is_staff:
        return HttpResponse("Доступ запрещен", status=403)

    # Получаем данные о продажах
    sales_data = (
        OrderItem.objects.values('product__name')
        .annotate(total_quantity=Sum('quantity'))
        .order_by('-total_quantity')
    )

    product_names = [item['product__name'] for item in sales_data]
    total_quantities = [item['total_quantity'] for item in sales_data]

    # Создаем график
    plt.figure(figsize=(10, 6))
    plt.bar(product_names, total_quantities, color='skyblue')
    plt.title('Продажи товаров', fontsize=16)
    plt.xlabel('Товары', fontsize=12)
    plt.ylabel('Количество проданных единиц', fontsize=12)
    plt.xticks(rotation=45, ha='right')

    # Сохраняем график в буфер
    buffer = BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    return HttpResponse(buffer, content_type='image/png')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
