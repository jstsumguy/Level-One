# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0051_auto_20150527_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='complete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.OneToOneField(to='lessons.Level'),
        ),
    ]
