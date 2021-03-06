# Generated by Django 3.0.5 on 2020-05-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_appointment_id', models.IntegerField()),
                ('patient_email', models.EmailField(max_length=254)),
                ('patient_name', models.CharField(default='', max_length=100)),
                ('patient_age', models.IntegerField()),
                ('patient_gender', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('doctor_id', models.CharField(max_length=100)),
                ('slot_date', models.DateField()),
                ('slot_time', models.TimeField(blank=True, null=True)),
                ('created_at', models.DateField()),
                ('udated_at', models.DateField()),
                ('status', models.CharField(max_length=10)),
                ('prescription', models.CharField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='DaySchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100)),
                ('hospital_name', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=15)),
                ('first_time_slot_from', models.TimeField()),
                ('first_time_slot_to', models.TimeField()),
                ('second_time_slot_from', models.TimeField()),
                ('second_time_slot_to', models.TimeField()),
                ('third_time_slot_from', models.TimeField()),
                ('third_time_slot_to', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('hospital', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='laboratory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_id', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30)),
                ('contact_no', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='labReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.EmailField(max_length=254)),
                ('reports', models.FileField(upload_to=None)),
                ('upload_date', models.DateField()),
                ('upload_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('phone_no', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='receptionist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recep_name', models.CharField(max_length=100)),
                ('recep_id', models.EmailField(max_length=254)),
                ('hospital_name', models.CharField(max_length=100)),
                ('hospital_id', models.IntegerField()),
            ],
        ),
    ]
