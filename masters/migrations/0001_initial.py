# Generated by Django 3.2.7 on 2021-09-14 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasterUsers',
            fields=[
                ('status', models.CharField(db_column='STATUS', default='Draft', max_length=100)),
                ('is_approved', models.BooleanField(db_column='IS_APPROVED', default=False)),
                ('is_active', models.BooleanField(blank=True, db_column='IS_ACTIVE', default=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, db_column='IS_DELETED', default=False, null=True)),
                ('created_by', models.CharField(blank=True, db_column='CREATED_BY', max_length=50, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='CREATED_DATE')),
                ('last_updated_by', models.CharField(blank=True, db_column='LAST_UPDATED_BY', max_length=50, null=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True, db_column='LAST_UPDATED_DATE')),
                ('user_id', models.AutoField(db_column='USER_ID', primary_key=True, serialize=False)),
                ('user_name', models.CharField(db_column='USER_NAME', max_length=20)),
                ('user_email', models.CharField(db_column='USER_EMAIL', max_length=30, unique=True)),
                ('password', models.CharField(db_column='PASSWORD', max_length=30, unique=True)),
                ('mobile', models.CharField(blank=True, db_column='MOBILE', max_length=12, null=True)),
                ('address', models.CharField(blank=True, db_column='ADDRESS', max_length=100, null=True)),
                ('is_admin', models.BooleanField(blank=True, db_column='IS_ADMIN', default=False, null=True)),
            ],
            options={
                'db_table': 'MST_USER',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('is_approved', models.BooleanField(db_column='IS_APPROVED', default=False)),
                ('is_active', models.BooleanField(blank=True, db_column='IS_ACTIVE', default=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, db_column='IS_DELETED', default=False, null=True)),
                ('created_by', models.CharField(blank=True, db_column='CREATED_BY', max_length=50, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='CREATED_DATE')),
                ('last_updated_by', models.CharField(blank=True, db_column='LAST_UPDATED_BY', max_length=50, null=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True, db_column='LAST_UPDATED_DATE')),
                ('product_id', models.AutoField(db_column='PRODUCT_ID', primary_key=True, serialize=False)),
                ('product_name', models.CharField(db_column='PRODUCT_NAME', max_length=50)),
                ('product_desc', models.CharField(db_column='PRODUCT_DESC', max_length=500)),
                ('product_type', models.CharField(db_column='PRODUCT_TYPE', max_length=50)),
                ('product_category', models.CharField(db_column='PRODUCT_CAT', max_length=20)),
                ('product_color', models.CharField(db_column='PRODUCT_COLOR', max_length=20)),
                ('product_size', models.CharField(db_column='PRODUCT_SIZE', max_length=5)),
                ('product_quantity', models.IntegerField(db_column='PRODUCT_QUANTITY')),
                ('product_price', models.FloatField(db_column='PRODUCT_PRICE')),
                ('status', models.CharField(db_column='STATUS', default='Draft', max_length=80)),
            ],
            options={
                'db_table': 'MST_PRODUCTS',
            },
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('status', models.CharField(db_column='STATUS', default='Draft', max_length=100)),
                ('is_approved', models.BooleanField(db_column='IS_APPROVED', default=False)),
                ('is_active', models.BooleanField(blank=True, db_column='IS_ACTIVE', default=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, db_column='IS_DELETED', default=False, null=True)),
                ('created_by', models.CharField(blank=True, db_column='CREATED_BY', max_length=50, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='CREATED_DATE')),
                ('last_updated_by', models.CharField(blank=True, db_column='LAST_UPDATED_BY', max_length=50, null=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True, db_column='LAST_UPDATED_DATE')),
                ('cart_product_id', models.AutoField(db_column='CART_PRODUCT_ID', primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(db_column='QUANTITY')),
                ('masteruser', models.ForeignKey(db_column='MASTERUSER', on_delete=django.db.models.deletion.CASCADE, related_name='USERCART', to='masters.masterusers')),
                ('product', models.ForeignKey(db_column='Product', on_delete=django.db.models.deletion.CASCADE, related_name='USERCART', to='masters.products')),
            ],
            options={
                'db_table': 'MST_USERCART',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('is_approved', models.BooleanField(db_column='IS_APPROVED', default=False)),
                ('is_active', models.BooleanField(blank=True, db_column='IS_ACTIVE', default=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, db_column='IS_DELETED', default=False, null=True)),
                ('created_by', models.CharField(blank=True, db_column='CREATED_BY', max_length=50, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='CREATED_DATE')),
                ('last_updated_by', models.CharField(blank=True, db_column='LAST_UPDATED_BY', max_length=50, null=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True, db_column='LAST_UPDATED_DATE')),
                ('order_id', models.AutoField(db_column='ORDER_ID', primary_key=True, serialize=False)),
                ('order_price', models.FloatField(db_column='ORDER_PRICE')),
                ('order_address', models.CharField(db_column='ORDER_ADDRESS', max_length=100)),
                ('order_quantity', models.IntegerField(db_column='ORDER_QUANTITY')),
                ('order_date', models.DateField(auto_now_add=True, db_column='ORDER_DATE')),
                ('status', models.CharField(db_column='STATUS', default='Draft', max_length=80)),
                ('masterUser', models.ForeignKey(db_column='MASTERUSER', on_delete=django.db.models.deletion.CASCADE, related_name='ORDERS', to='masters.masterusers')),
                ('product', models.ForeignKey(db_column='PRODUCT', on_delete=django.db.models.deletion.CASCADE, related_name='ORDERS', to='masters.products')),
            ],
            options={
                'db_table': 'MST_ORDER',
            },
        ),
    ]