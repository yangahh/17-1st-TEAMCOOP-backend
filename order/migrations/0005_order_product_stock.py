# Generated by Django 3.1.6 on 2021-02-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20210222_1110'),
        ('order', '0004_auto_20210217_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_stock',
            field=models.ManyToManyField(through='order.OrderProductStock', to='product.ProductStock'),
        ),
    ]