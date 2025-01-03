# Generated by Django 3.2.7 on 2021-09-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0002_auto_20210918_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercart',
            name='masteruser',
        ),
        migrations.RemoveField(
            model_name='usercart',
            name='product',
        ),
        migrations.AddField(
            model_name='products',
            name='product_image',
            field=models.CharField(blank=True, db_column='PRODUCT_IMAGE', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='product_serialNo',
            field=models.IntegerField(blank=True, db_column='SERIAL_NO', null=True),
        ),
        migrations.DeleteModel(
            name='MasterUsers',
        ),
        migrations.DeleteModel(
            name='UserCart',
        ),
    ]
