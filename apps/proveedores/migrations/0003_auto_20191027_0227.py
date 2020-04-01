# Generated by Django 2.2.6 on 2019-10-27 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_proveedor_movil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='ApellidoContacto',
            field=models.CharField(default='', max_length=255, verbose_name='Apellidos del Contacto'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='CorreoElectronico',
            field=models.EmailField(max_length=500, verbose_name='Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='Movil',
            field=models.CharField(default='', max_length=9, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='NombreContacto',
            field=models.CharField(default='', max_length=255, verbose_name='Nombred del Contacto'),
        ),
    ]