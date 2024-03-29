# Generated by Django 4.1.4 on 2023-04-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_review_reviewimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewimage',
            name='image',
        ),
        migrations.AddField(
            model_name='reviewimage',
            name='images',
            field=models.FileField(default=0, upload_to='products/reviews_image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(verbose_name='Review text'),
        ),
    ]
