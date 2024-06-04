from django.contrib import admin

from .models import Case, CaseParameter


class CaseParameterInline(admin.TabularInline):
    model = CaseParameter
    fields = ('value',)

@admin.register(Case)
class ProductAdmin(admin.ModelAdmin):
    inlines = (CaseParameterInline,)
