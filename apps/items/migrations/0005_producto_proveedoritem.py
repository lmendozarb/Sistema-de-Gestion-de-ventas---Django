# Generated by Django 2.2.6 on 2019-10-27 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0003_auto_20191027_0227'),
        ('items', '0004_auto_20191027_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='ProveedorItem',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='proveedores.Proveedor'),
        ),
    ]