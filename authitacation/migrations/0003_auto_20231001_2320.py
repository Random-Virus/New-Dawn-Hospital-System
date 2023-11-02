# Generated by Django 3.2.13 on 2023-10-01 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authitacation', '0002_auto_20231001_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birthdate', models.DateField(default='2000-01-01')),
                ('id_number', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=10)),
                ('marital_status', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=128)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='profile',
        ),
    ]
