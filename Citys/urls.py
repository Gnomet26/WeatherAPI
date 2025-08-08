from django.urls import path
from .views import UserCityView, WeatherByCityView

urlpatterns = [
    path('users/city/', UserCityView.as_view(), name='user-city'),
    path('weather/<str:city_name>/', WeatherByCityView.as_view(), name='weather-by-city'),
]
