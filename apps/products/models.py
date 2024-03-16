from django.db import models



class Product(models.Model):
    title = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    popular = models.BooleanField(default = False)
    views = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.title}. ID:{self.pk}"
    
    class Meta:
        ordering = ('-id',)
        

class ProductParameter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'product_parameters')
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"PRODUCT ID:{self.product.pk} ID:{self.pk}"
    