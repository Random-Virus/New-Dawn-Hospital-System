# Generated by Django 4.2.7 on 2023-11-05 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('selfqueue', '0008_patientqueue_symptoms'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=100)),
                ('doctor_code', models.CharField(max_length=100)),
                ('diagnosis', models.TextField()),
                ('prescription', models.TextField()),
                ('service', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('referrals', models.TextField(blank=True)),
                ('further_examination', models.TextField(blank=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selfqueue.patientqueue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
