from django.db import models

class SiteSettings(models.Model):
    telegram = models.URLField(max_length=255, blank=True)
    instagram = models.URLField(max_length=255, blank=True)
    whatsapp = models.URLField(max_length=255, blank=True)

    company_location = models.CharField("Местоположение компании", max_length=255, blank=True)
    schedule = models.CharField("График работы", max_length=100, blank=True)
    location_image = models.ImageField("Фотография местоположения", upload_to='settings', blank=True)

    about_us = models.TextField("О нас")
    about_us_image = models.ImageField("фотография \"О нас\"", blank=True)

    def __str__(self):
        return "Настройки сайта"