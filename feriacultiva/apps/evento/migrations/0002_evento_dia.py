# Generated by Django 2.2.6 on 2019-11-25 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='dia',
            field=models.CharField(default='sábados', max_length=20),
            preserve_default=False,
        ),
    ]
