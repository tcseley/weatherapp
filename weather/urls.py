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
    ]