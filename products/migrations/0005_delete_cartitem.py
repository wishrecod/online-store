# Generated by Django 5.1.4 on 2024-12-13 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_category_product_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
