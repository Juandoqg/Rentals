# Generated by Django 4.2.5 on 2023-10-21 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_vehicle_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='image',
        ),
    ]