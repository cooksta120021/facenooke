# Generated by Django 2.0.5 on 2018-06-24 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0004_auto_20180624_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='documents\\'),
        ),
    ]
