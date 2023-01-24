from django.shortcuts import render

from .models import Product, Category

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
    for image in product.images.all():
        print(image.image.url
    )
    context = {
        'product': product
    }
    return render(request, 'products/product_view.html', context)


def category_view(request, category):
    products = Product.objects.filter(category=Category.objects.get(category_name=category))
    context = {
        'products': products,
        'category': category
    }
    return render(request, 'products/category_view.html', context)


def search_view(request):
    if request.method == 'GET':
        query = request.GET['query']
        products = Product.objects.filter(product_name__contains=query)
        context = {
            'products': products
        }
        return render(request, 'products/search_view.html', context)
    else:
        return render(request, 'products/search_view.html')
