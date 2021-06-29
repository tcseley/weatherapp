from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'weather/index.html')

def about(request):
    return render(request, 'weather/about.html')

def cities_index(request):
    return render(request, 'weather/cities/index.html', {'cities': cities})


class City:
    def __init__(self, name, longitude, latitude, country):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.country = country

cities = [
    City('Lisben', 45.2558, 74.258, 'Spain'),
    City('Los Angels', 78.214, 98.2124, 'America'),
    City('Washington DC', 89.21547, 65.74, 'America'),
    City('Paris', 48.3265, 87.3698, 'France'),
]

