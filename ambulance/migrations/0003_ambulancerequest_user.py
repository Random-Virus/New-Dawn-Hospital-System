# Generated by Django 4.2.5 on 2023-10-13 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambulance', '0002_rename_userlocation_ambulancerequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulancerequest',
            name='user',
            field=models.CharField(default='Freddie', max_length=100),
            preserve_default=False,
        ),
    ]
