# Generated by Django 2.2.6 on 2019-11-28 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feriante', '0004_merge_20191103_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feriante',
            name='foto_feriante',
            field=models.ImageField(default='cliente/user.png', upload_to='feriante'),
        ),
    ]