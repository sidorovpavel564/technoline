from django.contrib import admin

from .models import Category, Product, Image, Size, Color, Attribute


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name', 'created', 'updated')
    list_filter = ('category_name', )
    search_fields = ('category_name', )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'category', 'description', 'preview_image', 'price', 'created', 'updated')
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


admin.site.register(Image, ImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Attribute, AttributeAdmin)
