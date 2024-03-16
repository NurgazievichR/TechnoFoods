from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    popular = models.BooleanField(default = False)


    def __str__(self) -> str:
        return self.title