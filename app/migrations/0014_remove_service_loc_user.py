# Generated by Django 3.2.6 on 2021-09-25 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_service_loc_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_loc',
            name='user',
        ),
    ]
