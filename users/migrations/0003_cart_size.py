# Generated by Django 3.2.7 on 2021-09-17 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_cartproxy_productproxy_userproxy'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.CharField(blank=True, db_column='SIZE', max_length=5, null=True),
        ),
    ]