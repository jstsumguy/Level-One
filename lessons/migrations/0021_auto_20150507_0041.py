# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0020_auto_20150507_0037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson_Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=800)),
                ('lesson', models.ForeignKey(to='lessons.Lesson')),
                ('student', models.ForeignKey(to='lessons.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 0, 41, 27, 582875), null=True),
        ),
    ]
