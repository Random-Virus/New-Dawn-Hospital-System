# Generated by Django 3.2.13 on 2023-10-01 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_alter_appointment_request_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='request_number',
            field=models.CharField(default='E8la2qMkjA', max_length=10, unique=True),
        ),
    ]
