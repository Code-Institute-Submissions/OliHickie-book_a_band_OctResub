# Generated by Django 3.2.6 on 2021-08-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0002_remove_category_friendly_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='band',
            name='image_four',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='band',
            name='location',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='band',
            name='name',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='band',
            name='tagline',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]