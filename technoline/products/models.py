from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    category_name = models.CharField(
        max_length=50, unique=True, verbose_name='Category Name')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(
        max_length=50, verbose_name='Product/Model name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, default=None)
    preview_image = models.ImageField('preview_image')
    price = models.IntegerField(verbose_name='Price')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product_name


class Image(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=None, related_name='images')
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='products/image')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Attribute(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name='attributes', verbose_name='Model')
    size = models.ForeignKey(
        Size, on_delete=models.DO_NOTHING, verbose_name='Size')
    color = models.ForeignKey(
        Color, on_delete=models.DO_NOTHING, verbose_name='Color')

    def get_model_fields(self):
        return [(field.verbose_name, getattr(self, field.name)) for field in Attribute._meta.fields if not field.primary_key]


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(verbose_name='Review text')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.text


class ReviewImage(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/reviews_image')


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Favorites(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
