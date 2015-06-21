# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0039_auto_20150521_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progress',
            name='course',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='student',
        ),
        migrations.DeleteModel(
            name='Progress',
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 22, 14, 14, 28, 489540), null=True),
        ),
    ]
