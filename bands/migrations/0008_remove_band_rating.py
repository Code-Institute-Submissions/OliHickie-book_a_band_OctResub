# Generated by Django 3.2.6 on 2021-09-24 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0007_bandreview_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='rating',
        ),
    ]
