# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_auto_20150425_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='users',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 25, 19, 55, 28, 287679), null=True),
        ),
    ]
