# Generated by Django 2.2.15 on 2020-10-04 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intense', '0011_profile_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture_url',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
