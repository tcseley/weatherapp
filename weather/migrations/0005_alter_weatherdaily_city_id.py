# Generated by Django 3.2.4 on 2021-06-29 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_alter_city_country_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherdaily',
            name='city_id',
            field=models.CharField(max_length=25),
        ),
    ]
