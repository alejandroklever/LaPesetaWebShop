# Generated by Django 2.2 on 2020-03-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0004_pedido_tienda'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='seleccionado',
            field=models.BooleanField(default=False),
        ),
    ]
