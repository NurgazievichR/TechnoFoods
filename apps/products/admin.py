from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import ProductParameter, Product, Category, ProductImage

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Category)


class ProductParameterInline(admin.TabularInline):
    model = ProductParameter
    fields = ('key','value')

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ('image',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductParameterInline, ProductImageInline)
    readonly_fields = ('views', 'id',)
