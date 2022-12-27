from django.shortcuts import render

from .models import Product

def index(request):
    product_list = Product.objects.all()
    asd = product_list[0]
    print(asd)
    product_list = asd.images.all()
    print(product_list)
    return render(request, 'products/index.html', {'product_list': product_list})
