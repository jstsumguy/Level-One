# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0008_auto_20150425_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 26, 3, 6, 0, 43436), null=True),
        ),
    ]
