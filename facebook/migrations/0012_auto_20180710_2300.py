# Generated by Django 2.0.5 on 2018-07-10 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0011_auto_20180708_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 10, 23, 0, 48)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='DOB',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
