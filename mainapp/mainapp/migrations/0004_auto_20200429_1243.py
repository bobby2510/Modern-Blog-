# Generated by Django 3.0.5 on 2020-04-29 07:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20200429_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 29, 7, 13, 20, 831281, tzinfo=utc)),
        ),
    ]