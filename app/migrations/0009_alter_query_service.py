# Generated by Django 3.2.6 on 2021-09-25 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_querydata1_loc_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.service_loc'),
        ),
    ]
