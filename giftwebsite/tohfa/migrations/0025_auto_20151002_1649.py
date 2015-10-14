# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0024_auto_20151002_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item4',
            name='sub_catagory',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='catagory', chained_field='catagory', auto_choose=True, to='tohfa.Sub_Catagory'),
        ),
        migrations.AlterField(
            model_name='item4',
            name='sub_sub_catagory',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='sub_catagory', chained_field='sub_catagory', auto_choose=True, to='tohfa.Sub_Sub_Catagory'),
        ),
    ]
