from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Promocode(models.Model):
    title = models.CharField(max_length=255)
    promocode = models.CharField(max_length=255)
    used = models.PositiveIntegerField(default=0)
    sale_persent = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self) -> str:
        return f"{self.title}, {self.promocode}"

