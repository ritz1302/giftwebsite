# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0018_auto_20151002_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item3',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('catagory', models.ForeignKey(to='tohfa.Catagory')),
                ('sub_catagory', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='catagory', chained_model_field='catagory', to='tohfa.Sub_Catagory')),
            ],
        ),
    ]
