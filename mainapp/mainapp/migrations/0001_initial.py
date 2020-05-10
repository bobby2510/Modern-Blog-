# Generated by Django 3.0.5 on 2020-04-27 03:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2020, 4, 27, 3, 23, 41, 79154, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('downvoted_users', models.ManyToManyField(blank=True, null=True, related_name='downvote', to=settings.AUTH_USER_MODEL)),
                ('upvoted_users', models.ManyToManyField(blank=True, null=True, related_name='upvote', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
