# Generated by Django 2.2.15 on 2020-10-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intense', '0010_auto_20201004_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_id',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
    ]
