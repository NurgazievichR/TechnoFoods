from django.shortcuts import get_object_or_404
from apps.products.models import Product
import re


product_pattern = r'^.*\/api\/v1\/products\/\d+\/$'

class ProductViewsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def view(self, request):
        path = request.path[:-1] if request.path[-1]=='/' else request.path
        product = get_object_or_404(Product, id=path.split('/')[-1])
        product.views+=1
        product.save()

    def __call__(self, request):
        response = self.get_response(request)
        if re.match(product_pattern, request.path):     
            self.view(request)
        return response