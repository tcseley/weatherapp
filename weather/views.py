from django.shortcuts import render
from django.http import HttpResponse
from .models import City

# Create your views here.
def index(request):
    return render(request, 'weather/index.html')

def about(request):
    return render(request, 'weather/about.html')

def cities_index(request):
    cities = City.objects.all()
    return render(request, 'weather/cities/index.html', {'cities': cities})

def cities_show(request, city_id):
    city = City.objects.get(id=city_id)
    return render(request, 'weather/cities/show.html', {'city': city})