# Generated by Django 3.2.6 on 2021-09-28 20:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_post_provider_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Query1',
        ),
        migrations.DeleteModel(
            name='Service_loc',
        ),
    ]
