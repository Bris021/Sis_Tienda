# Generated by Django 5.1.3 on 2024-11-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas_app', '0003_empleado_facturas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facturas',
            options={'verbose_name': 'Factura', 'verbose_name_plural': 'Facturas'},
        ),
        migrations.AlterField(
            model_name='facturas',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='facturas',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='facturas',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10),
        ),
        migrations.AlterModelTable(
            name='facturas',
            table='Facturas',
        ),
    ]
