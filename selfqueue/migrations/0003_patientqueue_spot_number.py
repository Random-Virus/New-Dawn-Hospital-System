# Generated by Django 3.2.13 on 2023-10-01 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfqueue', '0002_auto_20231001_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientqueue',
            name='spot_number',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
