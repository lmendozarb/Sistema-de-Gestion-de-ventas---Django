# Generated by Django 2.2.6 on 2019-10-29 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vilsoft', '0002_datosempresa_telefono'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datosempresa',
            old_name='NOmbre',
            new_name='Nombre',
        ),
    ]
