from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import UserCity, WeatherData
from .serializers import UserCitySerializer, WeatherSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils import timezone
from datetime import timezone as dt_timezone
from datetime import timedelta
from .WeatherByCityView_.api_module import result
from .WeatherByCityView_.matches.get_best_match import GetBestMatch
from django.urls import include

class UserCityView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_or_create_weather(self, city_name, request):
        city_name = city_name.title()
        weather = WeatherData.objects.filter(user=request.user).order_by('-timestamp').first()
        if weather and timezone.now() - weather.timestamp < timedelta(minutes=30):
            return weather

        r = result(city_name)

        data = r[city_name]
        WeatherData.objects.filter(user = request.user).delete()
        weather = WeatherData.objects.create(
            user = request.user,
            city_name=data['name'],
            country_code=data['sys']['country'],
            temperature=data['main']['temp'],
            feels_like=data['main']['feels_like'],
            humidity=data['main']['humidity'],
            pressure=data['main']['pressure'],
            wind_speed=data['wind']['speed'],
            wind_deg=data['wind']['deg'],
            weather_main=data['weather'][0]['main'],
            weather_description=data['weather'][0]['description'],
            clouds=data['clouds']['all'],
            visibility=data.get('visibility', 0),
            sunrise=timezone.datetime.fromtimestamp(data['sys']['sunrise'], tz=dt_timezone.utc),
            sunset=timezone.datetime.fromtimestamp(data['sys']['sunset'], tz=dt_timezone.utc),
        )
        return weather

    def get(self, request):
        try:
            user_city = request.user.selected_city
        except:
            return Response({"error": "Siz hali shahar tanlamagansiz."}, status=404)

        # weather ni bazadan olish yoki API dan olish
        weather = self.get_or_create_weather(user_city.city_name, request)

        if not weather:
            return Response({"error": "Ob-havo ma’lumotlarini olishda xatolik yuz berdi."}, status=500)

        # model instance bo‘lsa:
        serializer = WeatherSerializer(weather)

        return Response(serializer.data, status=200)

    def post(self, request):
        city_name = request.data.get('city_name')
        if not city_name:
            return Response({"error": "Shahar nomi kerak."}, status=400)
        city_n = GetBestMatch(city_name,"Citys/WeatherByCityView_/matches/city_aliases.json").get()["matched_string"]

        if city_n != None:
            UserCity.objects.filter(user=request.user).delete()
            WeatherData.objects.filter(user = request.user).delete()
            user_city = UserCity.objects.create(user=request.user, city_name=city_n)
            return Response(UserCitySerializer(user_city).data, status=201)
        return Response({"error":"Bunday shahar nomi tizimda mavjud emas"}, status=400)

    def put(self, request):
        city_name = request.data.get('city_name')
        if not city_name:
            return Response({"error": "Shahar nomi kerak."}, status=400)
        city_n = GetBestMatch(city_name,"Citys/WeatherByCityView_/matches/city_aliases.json").get()["matched_string"]

        if city_n != None:

            try:
                user_city = request.user.selected_city
                old_city = user_city.city_name
                user_city.city_name = city_n
                user_city.save()

                WeatherData.objects.filter(city_name__iexact=old_city).delete()

                return Response(UserCitySerializer(user_city).data)
            except UserCity.DoesNotExist:
                return Response({"error": "Siz hali hech qanday shahar tanlamagansiz."}, status=404)
        return Response({"error":"Bunday shahar nomi tizimda mavjud emas"}, status=400)
    def delete(self, request):
        try:
            user_city = request.user.selected_city
            WeatherData.objects.filter(city_name__iexact=user_city.city_name).delete()
            user_city.delete()
            return Response(status=204)
        except UserCity.DoesNotExist:
            return Response({"error": "Shahar tanlanmagan."}, status=404)


class WeatherByCityView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, city_name):
        city_name = city_name.title()
        best_match = GetBestMatch(city_name,"Citys/WeatherByCityView_/matches/city_aliases.json").get()["matched_string"]
        if best_match == None:
            return Response({"error": "Shahar topilmadi"}, status=404)
        r = result(best_match)

        if r[best_match]["cod"] != 200:
            return Response({"error": "Shahar topilmadi yoki APIdan xatolik."}, status=404)

        data = r[best_match]

        result_ = {
            "city_name": data['name'],
            "country_code": data['sys']['country'],
            "temperature": data['main']['temp'],
            "feels_like": data['main']['feels_like'],
            "humidity": data['main']['humidity'],
            "pressure": data['main']['pressure'],
            "wind_speed": data['wind']['speed'],
            "wind_deg": data['wind']['deg'],
            "weather_main": data['weather'][0]['main'],
            "weather_description": data['weather'][0]['description'],
            "clouds": data['clouds']['all'],
            "visibility": data.get('visibility', 0),
        }

        return Response(result_)
