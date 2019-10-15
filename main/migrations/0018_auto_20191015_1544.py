# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20191014_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='cata_icon',
            field=models.CharField(default=b'education', max_length=32, choices=[(b'education', b'\xe9\x97\x9c\xe6\x96\xbc\xe7\xb6\xb2\xe7\xab\x99'), (b'discovery', b'\xe6\x96\x87\xe7\xab\xa0\xe5\xb1\x95\xe8\xa6\xbd'), (b'culture', b'\xe9\xa1\x9e\xe5\x88\xa5\xe4\xbb\x8b\xe7\xb4\xb9'), (b'people', b'\xe6\x96\x87\xe7\xab\xa0\xe5\x88\x86\xe9\xa1\x9e'), (b'service', b'\xe4\xbd\x9c\xe5\x93\x81\xe5\x88\x86\xe4\xba\xab')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topics',
            name='cata_net',
            field=models.CharField(default=b'/IntroIR', max_length=32, choices=[(b'/IntroIR', b'\xe9\x97\x9c\xe6\x96\xbc\xe7\xb6\xb2\xe7\xab\x99'), (b'/Opendata', b'\xe6\x96\x87\xe7\xab\xa0\xe5\xb1\x95\xe8\xa6\xbd'), (b'/IssueAnaly', b'\xe9\xa1\x9e\xe5\x88\xa5\xe4\xbb\x8b\xe7\xb4\xb9'), (b'/IRdb', b'\xe6\x96\x87\xe7\xab\xa0\xe5\x88\x86\xe9\xa1\x9e'), (b'/Resource', b'\xe4\xbd\x9c\xe5\x93\x81\xe5\x88\x86\xe4\xba\xab')]),
            preserve_default=True,
        ),
    ]
