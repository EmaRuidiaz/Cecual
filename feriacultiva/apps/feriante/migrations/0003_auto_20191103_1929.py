# Generated by Django 2.2.6 on 2019-11-03 22:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feriante', '0002_feriante_encargado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feriante',
            name='descripcion',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='feriante',
            name='foto_feriante',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='feriante'),
            preserve_default=False,
        ),
    ]
