# Generated by Django 3.2.13 on 2023-10-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0009_alter_appointment_request_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='request_number',
            field=models.CharField(default='VB1eYT2XJg', max_length=10, unique=True),
        ),
    ]
