# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_auto_20150425_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='rep',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 25, 22, 40, 51, 571448), null=True),
        ),
    ]
