# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20191014_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='cata_icon',
            field=models.CharField(default=b'education', max_length=32, choices=[(b'education', b'\xe9\x97\x9c\xe6\x96\xbc\xe7\xb6\xb2\xe7\xab\x99'), (b'discovery', b'\xe6\x96\x87\xe7\xab\xa0\xe5\xb1\x95\xe8\xa6\xbd'), (b'culture', b'\xe9\xa1\x9e\xe5\x88\xa5\xe5\xb0\x8e\xe8\xa6\xbd'), (b'people', b'\xe6\x96\x87\xe7\xab\xa0\xe5\x88\x86\xe9\xa1\x9e'), (b'service', b'\xe4\xbd\x9c\xe5\x93\x81\xe5\x88\x86\xe4\xba\xab')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topics',
            name='cata_net',
            field=models.CharField(default=b'/IntroIR', max_length=32, choices=[(b'/IntroIR', b'\xe9\x97\x9c\xe6\x96\xbc\xe7\xb6\xb2\xe7\xab\x99'), (b'/Opendata', b'\xe6\x96\x87\xe7\xab\xa0\xe5\xb1\x95\xe8\xa6\xbd'), (b'/IssueAnaly', b'\xe9\xa1\x9e\xe5\x88\xa5\xe5\xb0\x8e\xe8\xa6\xbd'), (b'/IRdb', b'\xe6\x96\x87\xe7\xab\xa0\xe5\x88\x86\xe9\xa1\x9e'), (b'/Resource', b'\xe4\xbd\x9c\xe5\x93\x81\xe5\x88\x86\xe4\xba\xab')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topics',
            name='irdb_cata',
            field=models.CharField(default=b'\xe7\x84\xa1', max_length=32, choices=[(b'no', b'\xe7\x84\xa1'), (b'language', b'\xe8\xaa\x9e\xe8\xa8\x80\xe7\x9b\xb8\xe9\x97\x9c'), (b'itthing', b'\xe8\xb3\x87\xe8\xa8\x8a\xe9\x82\xa3\xe4\xba\x9b\xe4\xba\x8b'), (b'travel', b'\xe6\x97\x85\xe9\x81\x8a\xe6\x97\xa5\xe8\xa8\x98')]),
            preserve_default=True,
        ),
    ]
