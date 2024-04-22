# Generated by Django 4.2.11 on 2024-04-12 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ekartapp', '0009_product_price_product_stock_delete_packetsize'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.CreateModel(
            name='PacketSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packet', models.CharField(choices=[('Pillow Pouch', 'Pillow Pouch'), ('Standup Pouch', 'Standup Pouch'), ('Pouch', 'Pouch'), ('Bottle', 'Bottle'), ('Box', 'Box')], max_length=20)),
                ('grams', models.IntegerField(choices=[(20, '20g'), (60, '60g'), (130, '130g'), (150, '150g'), (300, '300g'), (400, '400g')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='product')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ekartapp.product')),
            ],
            options={
                'verbose_name': 'packet size',
                'verbose_name_plural': 'packet sizes',
            },
        ),
    ]