# Generated by Django 2.2.7 on 2019-11-28 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0007_auto_20191128_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacioncabecera',
            name='Estado',
            field=models.CharField(choices=[('COTIZACIÓN', 'COTIZACIÓN'), ('CONFIRMAR', 'CONFIRMAR'), ('FACTURADO', 'FACTURADO'), ('ANULAR', 'ANULAR')], max_length=15, verbose_name='Estado'),
        ),
    ]
