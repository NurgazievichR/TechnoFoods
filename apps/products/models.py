import random
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
from PIL import Image

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
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.title} {self.model}. ID:{self.pk}"

    def save(self, *args, **kwargs):
        # Добавляем slug
        cand = slugify(unidecode(f"{self.title}-{self.model}"))
        while Product.objects.filter(slug=cand).exists():
            cand += "".join([random.choice('1234567890') for _ in range(4)])
        self.slug = cand
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-id',)

class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')
    color = models.CharField(max_length=255, default='Blue')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'product_images')

    def save(self, *args, **kwargs):
        img_path = self.image.path
        with Image.open(img_path) as img:
            img = img.convert('RGB') 
            img = img.resize((1920, 1080), Image.ANTIALIAS)
            img.save(img_path, quality=85, optimize=True)
        super().save(*args, **kwargs)

class ProductParameter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'product_parameters')
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)