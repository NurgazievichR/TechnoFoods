from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=255)
    phone_numbers = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}  {self.phone_numbers}"
    
    