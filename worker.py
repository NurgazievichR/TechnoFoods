from apps.products.models import Product
# from worker import go

def go():
    products = Product.objects.all()
    for product in products:
        newName = product.title.upper()
        product.title = newName
        print(product.title)
        product.save()