# Generated by Django 2.2.6 on 2020-04-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20200423_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video',
        ),
        migrations.AddField(
            model_name='video',
            name='link_video',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]
