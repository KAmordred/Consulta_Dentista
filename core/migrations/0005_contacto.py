# Generated by Django 5.0.6 on 2024-07-08 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_producto_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[(0, 'Solicitud de cita'), (1, 'Solicitud de información sobre servicios'), (2, 'Consulta sobre tratamientos específicos'), (3, 'Solicitud de presupuesto'), (4, 'Realizar una consulta')])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
    ]