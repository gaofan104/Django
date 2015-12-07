# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockManagement', '0002_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='null', upload_to=b'img/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
