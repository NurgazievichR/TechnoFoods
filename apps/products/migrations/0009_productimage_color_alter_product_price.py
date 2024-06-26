# Generated by Django 5.0.3 on 2024-03-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0008_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="productimage",
            name="color",
            field=models.CharField(default="Blue", max_length=255),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
