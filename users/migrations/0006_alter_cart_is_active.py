# Generated by Django 3.2.7 on 2021-09-20 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210920_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='is_active',
            field=models.BooleanField(blank=True, db_column='IS_ACTIVE', default=True, null=True),
        ),
    ]
