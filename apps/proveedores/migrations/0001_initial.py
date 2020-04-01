# Generated by Django 2.2.6 on 2019-10-27 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general', '0002_moneda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RazonSocial', models.CharField(default='', max_length=100, verbose_name='Razón Social')),
                ('RUC', models.CharField(max_length=15, verbose_name='RUC')),
                ('DireccionLegal', models.CharField(max_length=500, verbose_name='Dirección Legal')),
                ('NombreContacto', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Nombred del Contacto')),
                ('ApellidoContacto', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Apellidos del Contacto')),
                ('NroDocumentoProveeedor', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Número Documento')),
                ('CorreoElectronico', models.EmailField(blank=True, max_length=500, null=True, verbose_name='Correo Electrónico')),
                ('TipoDocumentoProveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TipoDocumentoProveedor', to='general.TipoDocumento')),
            ],
            options={
                'verbose_name': 'Proveedores',
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]
