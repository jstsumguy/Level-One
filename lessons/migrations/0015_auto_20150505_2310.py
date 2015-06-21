# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0014_auto_20150505_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='quick_description',
            field=models.CharField(default=b'', max_length=400),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 23, 10, 3, 530043), null=True),
        ),
    ]
