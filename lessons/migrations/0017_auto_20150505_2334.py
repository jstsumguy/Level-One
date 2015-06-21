# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0016_auto_20150505_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 23, 34, 56, 630141), null=True),
        ),
        migrations.AlterField(
            model_name='progress',
            name='course',
            field=models.ForeignKey(to='lessons.Course'),
        ),
    ]
