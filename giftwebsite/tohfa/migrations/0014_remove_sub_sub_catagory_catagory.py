# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0013_catagory_sub_catagory_sub_sub_catagory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_sub_catagory',
            name='catagory',
        ),
    ]
