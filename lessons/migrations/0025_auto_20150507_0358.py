# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0024_auto_20150507_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='created',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 3, 58, 3, 846849), null=True),
        ),
    ]
