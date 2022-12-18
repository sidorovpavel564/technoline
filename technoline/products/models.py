from django.db import models

class Smartphone(models.Model):
    model_name = models.CharField(max_length=50, verbose_name='Model')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name='Color')
    display_resolution = models.CharField(max_length=50, verbose_name='Display Resolution')
    display_size = models.CharField(max_length=50, verbose_name='Display Size')
    display_type = models.CharField(max_length=50, verbose_name='Display Type')
    processor_model = models.CharField(max_length=50, verbose_name='Processor model')
    release_date = models.DateField(verbose_name='Release Date', null=True)
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='Created', null=True)
