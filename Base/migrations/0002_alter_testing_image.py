# Generated by Django 5.0.2 on 2024-03-03 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testing',
            name='image',
            field=models.ImageField(upload_to='vaccins'),
        ),
    ]
