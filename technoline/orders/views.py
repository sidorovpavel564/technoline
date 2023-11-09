from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import *

from .forms import OrderForm


@login_required
def checkout(request):
    user = request.user
    cart = user.cart.all()
    order_form_initial = {
        'address': user.profile.address,
        'phone': user.profile.phone,
        'email': user.email
    }
    order_form = OrderForm(request.POST or None, initial=order_form_initial)
    if request.method == 'POST':
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = user
            order.save()
            for cart_obj in cart:
                OrderItem.objects.create(order=order, product=cart_obj.product, item_price=cart_obj.product.price,
                                         quantity=cart_obj.quantity, total=cart_obj.product.price * cart_obj.quantity)
                cart_obj.delete()
            return redirect('index')
    context = {
        'order_form': order_form,
    }
    return render(request, 'orders/order_form.html', context)


@login_required
def user_orders_view(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    context = {
        'orders': orders,
    }
    return render(request, 'orders/user_orders_view.html', context)
