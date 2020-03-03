# Generated by Django 3.0.3 on 2020-03-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hos', '0016_auto_20200302_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='hospital',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctors',
            name='pincode',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='pincode',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
