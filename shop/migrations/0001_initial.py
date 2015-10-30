# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('product', '0004_auto_20151026_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.SmallIntegerField()),
                ('created_at', models.DateTimeField()),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('product', models.ForeignKey(to='product.Product')),
            ],
        ),
    ]
