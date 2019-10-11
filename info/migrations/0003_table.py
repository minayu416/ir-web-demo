# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('memberid', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=100)),
                ('jobname', models.TextField(max_length=255)),
                ('work', models.TextField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
