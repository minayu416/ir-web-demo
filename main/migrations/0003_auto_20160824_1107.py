# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_topics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('menu', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('intro', models.TextField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='topics',
            name='cata_icon',
            field=models.CharField(default=b'education', max_length=32, choices=[(b'education', b'IntroIR'), (b'discovery', b'Opendata'), (b'culture', b'IssueAnaly'), (b'people', b'IRdb')]),
            preserve_default=True,
        ),
    ]
