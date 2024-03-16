from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import ProductParameter, Product

admin.site.unregister(User)
admin.site.unregister(Group)


class ProductParameterInline(admin.TabularInline):
    model = ProductParameter
    fields = ('key','value')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductParameterInline, )
    readonly_fields = ('views', 'id',)
