# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silver', '0044_auto_20171115_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(help_text=b"The customer's last name.", max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='payment_processor',
            field=models.CharField(max_length=256, choices=[(b'manual', b'manual')]),
        ),
        migrations.AlterField(
            model_name='provider',
            name='city',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
