# Generated by Django 2.2.6 on 2019-11-03 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0004_remove_reserva_feriante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='precio',
        ),
    ]
