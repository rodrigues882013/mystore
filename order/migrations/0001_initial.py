# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[(b'Started', b'Started'), (b'Abandoned', b'Abandoned'), (b'Finished', b'Finished')], default=b'Started', max_length=120)),
                ('sub_total', models.DecimalField(decimal_places=2, default=10.99, max_digits=1000)),
                ('tax_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=1000)),
                ('final_total', models.DecimalField(decimal_places=2, default=10.99, max_digits=1000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
            ],
        ),
    ]