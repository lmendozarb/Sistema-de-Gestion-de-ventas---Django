# Generated by Django 2.2.6 on 2019-10-26 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='TipoProducto',
            field=models.IntegerField(choices=[(0, 'Hardware'), (1, 'Software')], default=2, verbose_name='Tipo del Producto'),
        ),
    ]
