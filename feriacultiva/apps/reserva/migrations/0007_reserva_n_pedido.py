# Generated by Django 2.2.6 on 2019-11-06 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0006_reserva_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='n_pedido',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
    ]