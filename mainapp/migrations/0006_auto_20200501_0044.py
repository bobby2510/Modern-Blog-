# Generated by Django 3.0.5 on 2020-04-30 19:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20200501_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 30, 19, 14, 6, 440562, tzinfo=utc)),
        ),
    ]