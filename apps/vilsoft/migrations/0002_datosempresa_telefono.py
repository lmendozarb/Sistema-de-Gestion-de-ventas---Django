# Generated by Django 2.2.6 on 2019-10-29 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vilsoft', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosempresa',
            name='Telefono',
            field=models.CharField(default='', max_length=30, verbose_name='Telefono'),
        ),
    ]
