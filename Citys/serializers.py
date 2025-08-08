from rest_framework import serializers
from .models import UserCity, WeatherData

class UserCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCity
        fields = ['city_name']

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'
