# Generated by Django 4.1.4 on 2023-01-20 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.color', verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='attributes', to='products.product'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.size', verbose_name='Size'),
        ),
        migrations.AlterField(
            model_name='product',
            name='preview_image',
            field=models.ImageField(upload_to='', verbose_name='preview_image'),
        ),
    ]
