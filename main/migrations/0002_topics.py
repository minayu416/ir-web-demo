# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=32)),
                ('cata_icon', models.CharField(default=b'IntroIR', max_length=32, choices=[(b'IntroIR', b'IntroIR'), (b'Opendata', b'Opendata'), (b'IssueAnaly', b'IssueAnaly'), (b'IRdb', b'IRdb')])),
                ('cata_net', models.CharField(max_length=255)),
                ('photo', models.FileField(upload_to=b'static/img/article_img/')),
                ('eventdate', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=255)),
                ('tar_web', models.CharField(max_length=255)),
                ('remark', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
