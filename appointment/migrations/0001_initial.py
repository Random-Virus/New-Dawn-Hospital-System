# Generated by Django 4.2.5 on 2023-09-27 15:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('speciality', models.CharField(max_length=120)),
                ('picture', models.ImageField(upload_to='media/doctors/')),
                ('details', models.TextField()),
                ('experience', models.TextField()),
                ('expertize', models.CharField(max_length=120)),
                ('twitter', models.CharField(blank=True, max_length=120, null=True)),
                ('facebook', models.CharField(blank=True, max_length=120, null=True)),
                ('instagram', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('note', models.TextField(blank=True)),
                ('request_number', models.CharField(default='8JuoXsNGSb', max_length=10, unique=True)),
                ('request_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.service')),
            ],
        ),
    ]
