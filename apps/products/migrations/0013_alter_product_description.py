# Generated by Django 5.0.3 on 2024-06-04 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0012_rename_price_som_product_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]
