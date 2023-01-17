from django.shortcuts import render

from .models import Product

def index(request):
    products = Product.objects.all()
    print(products)
    # asd = product_list[0]
    # print(asd)
    # product_list = asd.images.all()
    # print(product_list)
    return render(request, 'products/index.html', {'products': products})


def product_view(request):
    product = Product.objects.get(pk=1)
    f = product.attributes.get()
    print(f)
    print(f.color)
    print(f.get_model_fields())
    for image in product.images.all():
        print(image.image.url
    )
    context = {
        'product': product
    }
    return render(request, 'products/product_view.html', context)