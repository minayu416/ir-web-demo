# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Infopage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pageid', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=32)),
                ('headintro', models.TextField(max_length=255)),
                ('depart', models.CharField(max_length=50)),
                ('eventdate', models.DateField()),
                ('intro', models.TextField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
