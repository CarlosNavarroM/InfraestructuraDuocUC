# Generated by Django 5.1.2 on 2024-11-18 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monolito', '0002_remove_carrito_creado_remove_producto_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='valoracion',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]