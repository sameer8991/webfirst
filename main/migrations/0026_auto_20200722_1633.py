# Generated by Django 2.1.7 on 2020-07-22 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='comment',
        ),
    ]
