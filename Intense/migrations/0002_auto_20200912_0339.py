# Generated by Django 2.2.15 on 2020-09-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='coupon_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='product_color',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='product_size',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='product_unit',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(blank=True, choices=[('To pay', 'To pay'), ('To ship', 'To ship'), ('Received', 'Received'), ('Not Ordered', 'Not Ordered'), ('Cancelled', 'Cancelled')], default='To ship', max_length=155, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='non_verified_user_id',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_id',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='order_id',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='product_id',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='product_name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
