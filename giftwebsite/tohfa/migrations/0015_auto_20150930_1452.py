# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0014_remove_sub_sub_catagory_catagory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item2',
            name='sub_sub_catagory',
            field=models.ForeignKey(to='tohfa.Sub_Sub_Catagory'),
        ),
    ]
