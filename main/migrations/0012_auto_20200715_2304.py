# Generated by Django 3.0.4 on 2020-07-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200715_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='null', upload_to='blog/images'),
        ),
    ]