# Generated by Django 3.2.6 on 2021-09-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_auto_20210905_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='newbooking',
            name='band_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]