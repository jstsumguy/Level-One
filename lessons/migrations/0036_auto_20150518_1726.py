# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0035_auto_20150518_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multiple_Choice_Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=1000)),
                ('quiz', models.ForeignKey(to='lessons.Quiz')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quiz_Question_Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_type', models.IntegerField(default=0)),
                ('choice', models.CharField(max_length=800)),
                ('answer', models.BooleanField(default=False)),
                ('mcq', models.ForeignKey(to='lessons.Multiple_Choice_Question', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 17, 26, 47, 265277), null=True),
        ),
    ]
