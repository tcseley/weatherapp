# Generated by Django 3.2.4 on 2021-06-29 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherhourly',
            name='temperature',
            field=models.IntegerField(default=0),
        ),
    ]
