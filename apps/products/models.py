from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name} ID:{self.pk}"

class Product(models.Model):
    title = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    popular = models.BooleanField(default = False)
    views = models.IntegerField(default=0)
    price = models.PositiveBigIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'productsOfCategory')
    HaveProduct = models.BooleanField("В наличии",default = False)

    def __str__(self) -> str:
        return f"{self.title} {self.model}. ID:{self.pk}"

    class Meta:
        ordering = ('-id',)

class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')
    color = models.CharField(max_length=255, default='Blue')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'product_images')

class ProductParameter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'product_parameters')
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)