# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0015_auto_20150930_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item2',
            name='catagory',
        ),
        migrations.RemoveField(
            model_name='item2',
            name='sub_catagory',
        ),
    ]
