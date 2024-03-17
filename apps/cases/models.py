from django.db import models

class Case(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='cases')

    def __str__(self) -> str:
        return self.title
    

    