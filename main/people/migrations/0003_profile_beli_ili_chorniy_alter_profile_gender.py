# Generated by Django 5.0.1 on 2024-01-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_alter_profile_age_alter_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Beli_ili_chorniy',
            field=models.CharField(blank=True, choices=[('Б', 'Ч')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'М'), ('Ж', 'Ж')], max_length=1, null=True),
        ),
    ]
