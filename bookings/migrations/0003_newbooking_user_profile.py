# Generated by Django 3.2.6 on 2021-09-01 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('bookings', '0002_auto_20210822_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='newbooking',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.userprofile'),
        ),
    ]