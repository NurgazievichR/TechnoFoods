from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    # list_display = ('company_location',)
    

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj = ...):
        return True