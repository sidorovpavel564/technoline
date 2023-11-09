from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Category, Product, ReviewImage, Cart, Favorites
from .forms import ReviewForm


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        # 'products': products,
        'categories': categories,
        'page': page,
        'paginator': paginator,
    }
    return render(request, 'products/index.html', context)


def product_view(request, product_id):
    product = Product.objects.get(pk=product_id)
    reviews = product.reviews.order_by('-created').all()  # type: ignore
    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'products/product_view.html', context)


def category_view(request, category):
    products = Product.objects.filter(
        category=Category.objects.get(category_name=category))
    context = {
        'products': products,
        'category': category
    }
    return render(request, 'products/category_view.html', context)


def search_view(request):
    if request.method == 'GET':
        query = request.GET['query']
        products = Product.objects.filter(product_name__contains=query)
        categories = set(
            [product.category.category_name for product in products])
        context = {
            'products': products,
            'categories': categories
        }
        return render(request, 'products/search_view.html', context)
    else:
        return render(request, 'products/search_view.html')


@login_required
def post_review(request, product_id):
    comment_form = ReviewForm(request.POST or None)
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        if comment_form.is_valid():
            review = comment_form.save(commit=False)
            review.product = product
            review.author = request.user
            review.save()
            # requesting images from html form input
            # unfortunately user can add any type of file by dragging it into
            # the form
            images = request.FILES.getlist('images')
            for image in images:
                ReviewImage.objects.create(review=review, image=image)
            return redirect('product_view', product_id=product_id)
    context = {
        'comment_form': comment_form,
        'product': product,
    }
    return render(request, 'products/post_review.html', context)


@login_required
def cart_view(request):
    cart = request.user.cart.all()
    items_count = 0
    total = 0
    for cart_object in cart:
        items_count += cart_object.quantity
        total += cart_object.product.price * cart_object.quantity
    context = {
        'cart': cart,
        'items_count': items_count,
        'total': total,
    }
    return render(request, 'products/cart.html', context)


@login_required
def add_to_cart(request, product_id):
    cart_queryset = Cart.objects.filter(
        user=request.user, product=Product.objects.get(pk=product_id))
    if cart_queryset.exists():
        cart_obj = cart_queryset[0]
        cart_obj.quantity += 1
        cart_obj.save()
    else:
        Cart.objects.create(user=request.user, product=Product.objects.get(
            pk=product_id), quantity=1)
    return redirect(request.META['HTTP_REFERER'])


@login_required
def remove_from_cart(request, product_id):
    Cart.objects.get(user=request.user,
                     product=Product.objects.get(pk=product_id)).delete()
    return redirect('cart_view')


@login_required
def decrease_product_quantity_in_cart(request, product_id):
    cart_obj = Cart.objects.get(user=request.user,
                                product=Product.objects.get(pk=product_id))
    cart_obj.quantity -= 1
    cart_obj.save()
    return redirect(request.META['HTTP_REFERER'])


@login_required
def add_to_favorites(request, product_id):
    user = request.user
    Favorites.objects.create(
        user=user, product=Product.objects.get(pk=product_id))
    return redirect(request.META['HTTP_REFERER'])


@login_required
def favorites_view(request):
    favorites = Favorites.objects.filter(user=request.user)
    context = {
        'favorites': favorites
    }
    return render(request, 'products/favorites_view.html', context)
