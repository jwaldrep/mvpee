# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pottytimer', '0003_chart'),
    ]

    operations = [
        migrations.AddField(
            model_name='sticker',
            name='chart',
            field=models.ForeignKey(to='pottytimer.Chart', default=None),
        ),
    ]
