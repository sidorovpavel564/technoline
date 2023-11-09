from django.contrib import admin

from .models import Category, Product, Image, Size, Color, Attribute, Review, ReviewImage, Cart


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name', 'created', 'updated')
    list_filter = ('category_name', )
    search_fields = ('category_name', )


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('pk', )
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'category', 'description',
                    'preview_image', 'price', 'created', 'updated')
    # list_editable = ('product_name', 'category', 'description', 'preview_image', 'price')
    inlines = (ImageInline, )
    list_filter = ('product_name', )
    search_fields = ('product_name', )


class ImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'title', 'image', 'created', 'updated')
    # list_filter = ('product', )
    # search_fields = ('product', )


class SizeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', )


class ColorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', )


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'size', 'color')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'author', 'text', 'created', 'updated')


class ReviewImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'review', 'image')


class CartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'product', 'quantity')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewImage, ReviewImageAdmin)
admin.site.register(Cart, CartAdmin)
