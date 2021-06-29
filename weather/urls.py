from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cities/', views.cities_index, name='cities_index'),
    path('cities/<int:city_id>', views.cities_show, name='cities_show'),
    path('cities/create/', views.CityCreate.as_view(), name='cities_create'),
    path('cities/<int:pk>/update/', views.CityUpdate.as_view(), name='cities_update'),
    path('cities/<int:pk>/delete/', views.CityDelete.as_view(), name='cities_delete'),
    path('user/<username>/', views.profile, name='profile'),
    path('weatherdaily/', views.weatherdaily_index, name='weatherdaily_index'),
    path('weatherdaily/<int:weatherdaily_id>', views.weatherdaily_show, name='weatherdaily_show'),
    path('weatherdaily/create/', views.WeatherDailyCreate.as_view(), name='weatherdaily_create'),
    path('weatherdaily/<int:pk>/update/', views.WeatherDailyUpdate.as_view(), name='weatherdaily_update'),
    path('weatherdaily/<int:pk>/delete/', views.WeatherDailyDelete.as_view(), name='weatherdaily_delete'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    ]