# Generated by Django 2.2.15 on 2020-09-19 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intense', '0002_orderdetails_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='icon',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Icon'),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='logo',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Logo'),
        ),
    ]
