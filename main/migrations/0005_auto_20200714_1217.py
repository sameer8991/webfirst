# Generated by Django 3.0.4 on 2020-07-14 06:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200713_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 6, 47, 5, 34217, tzinfo=utc)),
        ),
    ]
