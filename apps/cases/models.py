from django.db import models
from PIL import Image

class Case(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='cases')

    def save(self, *args, **kwargs):
        img_path = self.image.path
        with Image.open(img_path) as img:
            img = img.convert('RGB') 
            img = img.resize((1920, 1080), Image.ANTIALIAS)
            img.save(img_path, quality=85, optimize=True)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class CaseParameter(models.Model):
    product = models.ForeignKey(Case, on_delete=models.CASCADE, related_name = 'case_parameters')
    value = models.CharField(max_length=255)