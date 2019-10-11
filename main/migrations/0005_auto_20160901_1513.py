# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160826_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='cata_icon',
            field=models.CharField(default=b'education', max_length=32, choices=[(b'education', b'IntroIR'), (b'discovery', b'Opendata'), (b'culture', b'IssueAnaly'), (b'people', b'IRdb'), (b'service', b'Resource')]),
            preserve_default=True,
        ),
    ]
