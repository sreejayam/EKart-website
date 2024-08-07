# Generated by Django 4.2.11 on 2024-04-12 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ekartapp', '0007_remove_product_packet_size'),
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
                ('grams', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ekartapp.product')),
            ],
            options={
                'verbose_name': 'packet size',
                'verbose_name_plural': 'packet sizes',
            },
        ),
    ]
