# Generated by Django 4.2.11 on 2024-04-12 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ekartapp', '0008_remove_product_price_remove_product_stock_packetsize'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PacketSize',
        ),
    ]
