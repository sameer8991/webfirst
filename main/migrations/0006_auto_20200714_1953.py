# Generated by Django 3.0.4 on 2020-07-14 14:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200714_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 14, 23, 4, 505426, tzinfo=utc)),
        ),
    ]
