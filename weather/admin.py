from django.contrib import admin
from .models import WeatherHourly, WeatherDaily, City, Users, UsersCity, Country

# Register your models here.

admin.site.register(WeatherHourly)
admin.site.register(WeatherDaily)
admin.site.register(City)
admin.site.register(Users)
admin.site.register(UsersCity)
admin.site.register(Country)

