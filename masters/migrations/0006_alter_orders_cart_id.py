# Generated by Django 3.2.7 on 2021-09-20 11:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0005_alter_orders_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='cart_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, db_column='CART_ID', null=True), blank=True, null=True, size=None),
        ),
    ]