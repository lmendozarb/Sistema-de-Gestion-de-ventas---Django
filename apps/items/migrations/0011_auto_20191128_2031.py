# Generated by Django 2.2.7 on 2019-11-28 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_auto_20191128_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Cantidad',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Cantidad'),
        ),
    ]