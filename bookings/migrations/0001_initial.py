# Generated by Django 3.2.6 on 2021-08-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=14)),
                ('venue_name', models.CharField(max_length=50)),
                ('venue_address1', models.CharField(max_length=80)),
                ('venue_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('county', models.CharField(max_length=80)),
                ('postcode', models.CharField(max_length=10)),
                ('wedding_date', models.CharField(max_length=10)),
                ('start_time', models.CharField(max_length=10)),
                ('duration', models.IntegerField()),
                ('emergency_contact', models.CharField(max_length=50)),
                ('emergency_phone', models.CharField(max_length=14)),
                ('additional_information', models.TextField(blank=True, null=True)),
                ('booking_created_at', models.DateTimeField(auto_now_add=True)),
                ('booking_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]