# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0042_auto_20150523_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_lesson_activity',
            name='student',
            field=models.ForeignKey(to='lessons.Student', null=True),
            preserve_default=True,
        ),
    ]
