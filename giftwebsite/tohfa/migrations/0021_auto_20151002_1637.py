# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0020_auto_20151002_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item4',
            name='sub_catagory',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='catagory', to='tohfa.Sub_Catagory', chained_model_field='catagory', auto_choose=True, blank=True),
        ),
        migrations.AlterField(
            model_name='item4',
            name='sub_sub_catagory',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='sub_catagory', to='tohfa.Sub_Sub_Catagory', chained_model_field='sub_catagory', auto_choose=True, blank=True),
        ),
    ]