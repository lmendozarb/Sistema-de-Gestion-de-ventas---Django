# Generated by Django 2.2.7 on 2019-12-06 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0008_auto_20191128_0451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itempago',
            name='cuerpo',
        ),
        migrations.AddField(
            model_name='itempago',
            name='cabecera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cotizaciones.CotizacionCabecera'),
        ),
    ]
