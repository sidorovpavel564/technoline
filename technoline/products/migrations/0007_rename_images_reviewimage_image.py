# Generated by Django 4.1.4 on 2023-04-05 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_reviewimage_image_reviewimage_images_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewimage',
            old_name='images',
            new_name='image',
        ),
    ]
