# Generated by Django 5.0.6 on 2024-07-08 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_producto_marca_producto_nuevo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]