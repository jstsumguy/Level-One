# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0048_auto_20150527_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField(default=0)),
                ('xp', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='student',
            name='rep',
        ),
        migrations.AddField(
            model_name='student',
            name='level',
            field=models.ForeignKey(to='lessons.Level', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 15, 16, 19, 461670), auto_now=True),
        ),
    ]
