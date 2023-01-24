from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>', views.product_view, name='product-view'),
    path('category/<str:category>', views.category_view, name='category-view'),
    path('search', views.search_view, name='search-view'),
]