from django.contrib.auth.models import User
from rest_framework import serializers

from products.models import Product, Review, Cart


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class PrdouctSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'category',
                  'description', 'preview_image', 'price']


class ProductReviewsSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Review
        fields = ['pk', 'author', 'text', 'created', 'updated']


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    product = serializers.CharField(read_only=True)

    class Meta:
        model = Review
        fields = ['pk', 'product', 'author', 'text', 'created', 'updated']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product', 'quantity']
