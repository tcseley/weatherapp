from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import City, WeatherDaily
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
def index(request):
    return render(request, 'weather/index.html')

def about(request):
    return render(request, 'weather/about.html')

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    cities = City.objects.filter(user=user)
    return render(request, 'weather/profile.html', {'username': username, 'cities': cities})

def cities_index(request):
    cities = City.objects.all()
    return render(request, 'weather/cities/index.html', {'cities': cities})

def cities_show(request, city_id):
    city = City.objects.get(id=city_id)
    return render(request, 'weather/cities/show.html', {'city': city})


class CityCreate(CreateView):
  model = City
  fields = '__all__'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect('/cities'+ str(self.object.pk))

@method_decorator(login_required, name='dispatch')
class CityUpdate(UpdateView):
  model = City
  fields = ['city_name', 'city_latitude', 'city_longitude', 'zip_code', 'country_id', 'weatherdailies']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/cities/' + str(self.object.pk))

@method_decorator(login_required, name='dispatch')
class CityDelete(DeleteView):
  model = City
  success_url = '/cities'



def weatherdaily_index(request):
    weatherdailies = WeatherDaily.objects.all()
    return render(request, 'weather/weatherdaily/index.html', {'weatherdailies': weatherdailies})

def weatherdaily_show(request, weatherdaily_id):
    weatherdaily = WeatherDaily.objects.get(id=weatherdaily_id)
    return render(request, 'weather/weatherdaily/show.html', {'weatherdaily': weatherdaily})

class WeatherDailyCreate(CreateView):
    model = WeatherDaily
    fields = '__all__'
    success_url = '/weatherdaily'
class WeatherDailyUpdate(UpdateView):
    model = WeatherDaily
    fields = ['date', 'min_temp', 'max_temp', 'sunrise_time', 'sunset_time', 'last_updated', 'city_id']
    success_url = '/weatherdaily'

class WeatherDailyDelete(DeleteView):
    model = WeatherDaily
    success_url = '/weatherdaily'


def login_view(request):
     # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
                    return HttpResponseRedirect('/login')
        else:
            print('The username and/or password is incorrect.')
            return HttpResponseRedirect('/login')
    else: # it was a get request so send the emtpy login form
        form = AuthenticationForm()
        return render(request, 'weather/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/cities')

  
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            u = form.cleaned_data['username']
            login(request, user)
            return redirect('/cities')
        else:
          print("Invalid form submitted.")
          return redirect('/signup')
    else:
        form = UserCreationForm()
        return render(request, 'weather/signup.html', {'form': form})