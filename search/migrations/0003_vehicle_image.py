# Generated by Django 4.2.5 on 2023-10-20 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_vehicle_price_alter_vehicle_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle_images/'),
        ),
    ]