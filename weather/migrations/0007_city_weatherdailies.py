# Generated by Django 3.2.4 on 2021-06-29 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0006_city_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='weatherdailies',
            field=models.ManyToManyField(to='weather.WeatherDaily'),
        ),
    ]
