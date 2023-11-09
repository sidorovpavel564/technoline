from django.urls import path

from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('my-orders/', views.user_orders_view, name='user_orders_view'),
]
