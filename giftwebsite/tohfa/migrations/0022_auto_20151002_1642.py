# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0021_auto_20151002_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item4',
            name='sub_catagory',
            field=smart_selects.db_fields.GroupedForeignKey(to='tohfa.Sub_Catagory', group_field=models.ForeignKey(to='tohfa.Catagory')),
        ),
        migrations.AlterField(
            model_name='item4',
            name='sub_sub_catagory',
            field=smart_selects.db_fields.GroupedForeignKey(to='tohfa.Sub_Sub_Catagory', group_field=smart_selects.db_fields.GroupedForeignKey(to='tohfa.Sub_Catagory', group_field=models.ForeignKey(to='tohfa.Catagory'))),
        ),
    ]
