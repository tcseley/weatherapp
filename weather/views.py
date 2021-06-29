from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import City
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class CityCreate(CreateView):
  model = City
  fields = '__all__'
  success_url = '/cities'

class CityUpdate(UpdateView):
  model = City
  fields = ['city_name', 'city_latitude', 'city_longitude', 'zip_code', 'country_id']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/cities/' + str(self.object.pk))

class CityDelete(DeleteView):
  model = City
  success_url = '/cities'