# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0030_auto_20150511_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson_Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('source', models.TextField()),
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
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 1, 12, 36, 278739), null=True),
        ),
    ]
