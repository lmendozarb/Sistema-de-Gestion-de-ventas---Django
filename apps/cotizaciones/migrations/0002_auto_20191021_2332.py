# Generated by Django 2.2.6 on 2019-10-21 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacioncabecera',
            name='Descuento',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='Descuento'),
        ),
    ]
