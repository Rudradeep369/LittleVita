# Generated by Django 5.0.2 on 2024-03-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0013_remove_doctor_days_in_hospital_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='doctor_images/'),
        ),
    ]