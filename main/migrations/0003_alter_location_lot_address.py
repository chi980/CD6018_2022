# Generated by Django 4.1.3 on 2022-12-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_location_latitude_alter_location_longitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lot_address',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
