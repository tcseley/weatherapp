import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class WeatherHourly(models.Model):
    name = models.CharField(max_length=25)
    temperature = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    wind_speed = models.IntegerField(default=0)
    wind_direction = models.CharField(max_length=10)
    city_id = models.IntegerField(default=0)


    def __str__ (self):
        return self.name


class WeatherDaily(models.Model):
    date = models.DateTimeField('Calendar Date')
    min_temp = models.IntegerField(default=0)
    max_temp = models.IntegerField(default=0)
    sunrise_time = models.TimeField('Sunrise:')
    sunset_time = models.TimeField('Sunset:')
    last_updated = models.DateTimeField('Last updated')
    city_id = models.CharField(max_length=25)
    

    def __str__(self):
        return self.city_id


class City(models.Model):
    city_name = models.CharField(max_length=25)
    city_longitude = models.IntegerField(default=0)
    city_latitude = models.IntegerField(default=0)
    zip_code = models.IntegerField(default=0)
    country_id = models.CharField(max_length=25)

    def __str__(self):
        return self.city_name


class Country(models.Model):
    country_name = models.CharField(max_length=30)

    def __str__(self):
        return self.country_name


class UsersCity(models.Model):
    city_id = models.IntegerField(default=0)
    added_on = models.DateTimeField('Added on')
    users_id = models.IntegerField(default=0)

    def __str__(self):
        return self.users_id


class Users(models.Model):
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email






