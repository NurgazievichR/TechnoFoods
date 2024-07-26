from django.db import models
from PIL import Image

from utils.services import convert_image, to_webp

class Case(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='cases')

    def save(self, *args, **kwargs):
        to_webp(self.image)
        super().save(*args, **kwargs)
        convert_image(self.image.path)

    
    def __str__(self) -> str:
        return self.title


class CaseParameter(models.Model):
    product = models.ForeignKey(Case, on_delete=models.CASCADE, related_name = 'case_parameters')
    value = models.CharField(max_length=255)