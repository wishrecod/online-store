from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)  # Название товара
    description = models.TextField(blank=True)  # Описание товара
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена товара
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # Изображение товара
    stock = models.PositiveIntegerField(default=0)  # Количество на складе
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True) 

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # Пользователь
    created_at = models.DateTimeField(default=now)  # Дата создания заказа
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Итоговая сумма
    is_paid = models.BooleanField(default=False)  # Статус оплаты

    def __str__(self):
        return f"Заказ #{self.id} от {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)  # Заказ
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Товар
    quantity = models.PositiveIntegerField(default=1)  # Количество
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена за единицу товара

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
    

