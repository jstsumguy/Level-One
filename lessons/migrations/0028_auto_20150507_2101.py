# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0027_auto_20150507_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='challenge_type',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 21, 1, 43, 123813), null=True),
        ),
    ]
