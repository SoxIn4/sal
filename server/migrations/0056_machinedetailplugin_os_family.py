# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-22 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0055_auto_20170822_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinedetailplugin',
            name='os_family',
            field=models.CharField(choices=[(b'Darwin', b'macOS'), (b'Windows', b'Windows'), (b'Linux', b'Linux')], db_index=True, default=b'Darwin', max_length=256, verbose_name=b'OS Family'),
        ),
    ]
