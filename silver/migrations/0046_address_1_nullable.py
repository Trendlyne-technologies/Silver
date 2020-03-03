# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silver', '0045_auto_20180402_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address_1',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='address_1',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
