# Generated by Django 2.2.6 on 2019-11-23 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='voto',
            field=models.CharField(default='NoVote', max_length=10),
        ),
    ]
