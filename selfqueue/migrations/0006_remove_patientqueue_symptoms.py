# Generated by Django 3.2.13 on 2023-10-14 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selfqueue', '0005_auto_20231011_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientqueue',
            name='symptoms',
        ),
    ]