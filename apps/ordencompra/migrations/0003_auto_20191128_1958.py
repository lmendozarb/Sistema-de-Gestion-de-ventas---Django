# Generated by Django 2.2.7 on 2019-11-28 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordencompra', '0002_auto_20191128_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordencabecera',
            name='Estado',
            field=models.CharField(choices=[('CONFIRMAR', 'CONFIRMAR'), ('FACTURADO', 'FACTURADO'), ('ANULAR', 'ANULAR')], max_length=15, verbose_name='Estado'),
        ),
    ]
