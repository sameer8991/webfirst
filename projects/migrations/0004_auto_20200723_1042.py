# Generated by Django 2.1.7 on 2020-07-23 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='emali',
            new_name='email',
        ),
    ]
