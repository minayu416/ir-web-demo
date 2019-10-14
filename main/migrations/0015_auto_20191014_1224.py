# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20170515_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='cata_icon',
            field=models.CharField(default=b'education', max_length=32, choices=[(b'education', b'\xe9\x97\x9c\xe6\x96\xbc\xe7\xb6\xb2\xe7\xab\x99'), (b'discovery', b'\xe5\x85\xac\xe9\x96\x8b\xe8\xb3\x87\xe8\xa8\x8a'), (b'culture', b'\xe8\xad\xb0\xe9\xa1\x8c\xe5\x88\x86\xe6\x9e\x90'), (b'people', b'IR\xe8\xb3\x87\xe6\x96\x99\xe5\xba\xab'), (b'service', b'\xe8\xb3\x87\xe6\xba\x90\xe5\x88\x86\xe4\xba\xab')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topics',
            name='cata_net',
            field=models.CharField(default=b'/IntroIR', max_length=32, choices=[(b'/IntroIR', b'\xe9\x97\x9c\xe6\x96\xbc\xe7\xb6\xb2\xe7\xab\x99'), (b'/Opendata', b'\xe5\x85\xac\xe9\x96\x8b\xe8\xb3\x87\xe8\xa8\x8a'), (b'/IssueAnaly', b'\xe8\xad\xb0\xe9\xa1\x8c\xe5\x88\x86\xe6\x9e\x90'), (b'/IRdb', b'IR\xe8\xb3\x87\xe6\x96\x99\xe5\xba\xab'), (b'/Resource', b'\xe8\xb3\x87\xe6\xba\x90\xe5\x88\x86\xe4\xba\xab')]),
            preserve_default=True,
        ),
    ]
