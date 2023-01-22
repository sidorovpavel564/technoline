from django.shortcuts import render

from .models import Product, Category

from django.forms.models import model_to_dict

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'products/index.html', context)


def product_view(request, product_id):
    product = Product.objects.get(pk=product_id)
    # f = product.attributes.get()
    # print(f)
    # print(model_to_dict(f))
    # print(f.color)
    # print(f.get_model_fields())
    # print(getattr(f, 'product'))
    for image in product.images.all():
        print(image.image.url
    )
    context = {
        'product': product
    }
    return render(request, 'products/product_view.html', context)
