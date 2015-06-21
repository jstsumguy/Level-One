# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0011_auto_20150426_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 0, 34, 5, 898844), null=True),
        ),
    ]
