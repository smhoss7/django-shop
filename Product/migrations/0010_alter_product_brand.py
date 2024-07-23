# Generated by Django 5.0.7 on 2024-07-21 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0009_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ManyToManyField(blank=True, related_name='products', to='Product.brand'),
        ),
    ]
