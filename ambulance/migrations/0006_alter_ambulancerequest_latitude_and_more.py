# Generated by Django 4.2.5 on 2023-10-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambulance', '0005_ambulancerequest_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulancerequest',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ambulancerequest',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
