from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>', views.product_view, name='product_view'),
    path('category/<str:category>', views.category_view, name='category_view'),
    path('search', views.search_view, name='search-view'),
    path('product/<int:product_id>/post_review',
         views.post_review, name='post_review'),
    path('product/<int:product_id>/add_to_cart',
         views.add_to_cart, name='add_to_cart'),
    path('cart', views.cart_view, name='cart_view'),
    path('cart/remove/<int:product_id>',
         views.remove_from_cart, name='remove_from_cart'),
    path('cart/decrease_product_quantity_in_cart/<int:product_id>',
         views.decrease_product_quantity_in_cart, name='decrease_product_quantity_in_cart'),
    path('favorites/add/<int:product_id>',
         views.add_to_favorites, name='add_to_favorites'),
    path('favorites', views.favorites_view, name='favorites_view'),
]
