# Generated by Django 2.2.7 on 2019-11-22 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0003_auto_20191027_0227'),
        ('cotizaciones', '0003_cuerpocotizacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='productoQTN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SerializeProductoQTN', models.IntegerField(default=0, verbose_name='Serial')),
                ('Nombre', models.CharField(max_length=200, verbose_name='Nombre del Producto')),
                ('Foto', models.ImageField(blank=True, default='/non/newitem.jpg', null=True, upload_to='Items', verbose_name='Foto')),
                ('TipoProducto', models.IntegerField(choices=[(0, 'Hardware'), (1, 'Software')], default=2, verbose_name='Tipo del Producto')),
                ('Descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('Precio', models.FloatField(verbose_name='Precio')),
                ('Cantidad', models.IntegerField(blank=True, null=True, verbose_name='Cantidad')),
                ('FechaRegistro', models.DateTimeField(auto_now=True)),
                ('ProveedorItem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.Proveedor')),
            ],
            options={
                'verbose_name': 'ProductoQTN',
                'verbose_name_plural': 'ProductoQTN',
            },
        ),
    ]
