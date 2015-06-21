# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_auto_20150425_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='course',
            new_name='lesson',
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 25, 22, 3, 48, 260477), null=True),
        ),
    ]
