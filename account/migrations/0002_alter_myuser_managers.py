# Generated by Django 4.0 on 2022-01-05 06:22

import account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='myuser',
            managers=[
                ('objects', account.models.MyUserManager()),
            ],
        ),
    ]
