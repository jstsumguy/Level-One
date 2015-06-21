# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0019_auto_20150506_2229'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Quiz_Question',
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 0, 37, 41, 954843), null=True),
        ),
    ]
