# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0023_auto_20151002_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item4',
            name='sub_catagory',
            field=smart_selects.db_fields.ChainedForeignKey(to='tohfa.Sub_Catagory', auto_choose=True, chained_field='catagory', chained_model_field='catagory', blank=True),
        ),
        migrations.AlterField(
            model_name='item4',
            name='sub_sub_catagory',
            field=smart_selects.db_fields.ChainedForeignKey(to='tohfa.Sub_Sub_Catagory', auto_choose=True, chained_field='sub_catagory', chained_model_field='sub_catagory', blank=True),
        ),
    ]
