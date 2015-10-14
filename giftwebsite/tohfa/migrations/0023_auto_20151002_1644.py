# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0022_auto_20151002_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item4',
            name='sub_catagory',
            field=smart_selects.db_fields.GroupedForeignKey(to='tohfa.Sub_Catagory', group_field='catagory'),
        ),
        migrations.AlterField(
            model_name='item4',
            name='sub_sub_catagory',
            field=smart_selects.db_fields.GroupedForeignKey(to='tohfa.Sub_Sub_Catagory', group_field='sub_catagory'),
        ),
    ]
