# Generated by Django 2.2.15 on 2020-10-01 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intense', '0005_auto_20201001_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupproduct',
            name='startdate',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
