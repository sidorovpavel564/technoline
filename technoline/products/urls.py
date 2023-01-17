from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product_view, name='product_view'),
]