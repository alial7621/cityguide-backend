# Generated by Django 2.2.5 on 2020-08-21 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200821_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 21, 21, 39, 50, 420105)),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 21, 21, 39, 50, 420105)),
        ),
    ]
