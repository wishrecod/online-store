from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # Пользователь
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Продукт
    quantity = models.PositiveIntegerField(default=1)  # Количество

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
