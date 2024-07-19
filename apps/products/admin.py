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
    fields = ('image','color')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductParameterInline, ProductImageInline)
    readonly_fields = ('views', 'id',)
    search_fields = ('title',)
    actions = ['duplicate_selected_products']
    prepopulated_fields = {'slug': ('title','model')}

    def duplicate_selected_products(self, request, queryset):
        for product in queryset:
            product.pk = None
            product.save()
