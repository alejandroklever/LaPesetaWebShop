# Generated by Django 2.2 on 2020-03-14 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20191210_1116'),
        ('compra', '0003_auto_20200314_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='tienda',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tienda.Tienda'),
            preserve_default=False,
        ),
    ]
