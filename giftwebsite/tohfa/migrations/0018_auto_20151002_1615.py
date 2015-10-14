# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0017_item3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item3',
            name='catagory',
        ),
        migrations.RemoveField(
            model_name='item3',
            name='sub_catagory',
        ),
        migrations.RemoveField(
            model_name='item3',
            name='sub_sub_catagory',
        ),
        migrations.DeleteModel(
            name='Item3',
        ),
    ]
