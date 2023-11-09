# Generated by Django 4.1.4 on 2023-04-17 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_orderitem_price_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=123123, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.TextField(blank=True, verbose_name='Email'),
        ),
    ]
