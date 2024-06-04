from django.db import models

class Case(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='cases')

    def __str__(self) -> str:
        return self.title


class CaseParameter(models.Model):
    product = models.ForeignKey(Case, on_delete=models.CASCADE, related_name = 'case_parameters')
    value = models.CharField(max_length=255)