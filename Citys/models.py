from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='selected_city')
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.city_name}"

class WeatherData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    temperature = models.FloatField()
    feels_like = models.FloatField()
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    wind_speed = models.FloatField()
    wind_deg = models.IntegerField()
    weather_main = models.CharField(max_length=50)
    weather_description = models.CharField(max_length=100)
    clouds = models.IntegerField()
    visibility = models.IntegerField()
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city_name} ({self.timestamp.strftime('%Y-%m-%d %H:%M')})"
