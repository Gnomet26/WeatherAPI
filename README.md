# WeatherAPI

## Loyiha haqida  
WeatherAPI loyihasi JWT token asosida ishlaydigan autentifikatsiya tizimini yaratish, REST API ishlab chiqish va tashqi API’lar bilan integratsiya qilish ko‘nikmalarini rivojlantirishga mo‘ljallangan. Loyiha Django frameworkida Python 3 yordamida ishlab chiqilgan. 

## Asosiy imkoniyatlar  
- Foydalanuvchi ro‘yxatdan o‘tishi, login, logout, tokenni yangilash (refresh token) JWT orqali  
- Foydalanuvchilar o‘z profillarida shaharni tanlash imkoniyati  
- Tanlangan shahar bo‘yicha OpenWeatherMap API’dan ob-havo ma’lumotlarini olish  
- Maxsus `weather/Tashkent` endpoint orqali istalgan shahar ob-havosini olish

## Texnologiyalar  
- Python 3  
- Django  
- Django REST Framework  
- JWT (JSON Web Tokens)  
- PostgreSQL  
- OpenWeatherMap API

## O‘rnatish va ishga tushirish  
1. Loyiha kodini yuklab olish:  
   ```bash  
   git clone <repository_url>  
   cd WeatherAPI  
##Virtual muhit yaratish va faollashtirish:
python3 -m venv venv  
source venv/bin/activate  # Linux/macOS  
venv\Scripts\activate     # Windows  

##Kerakli paketlarni o‘rnatish:
pip install -r requirements.txt  

##PostgreSQL serverni ishga tushurish va baza yaratish

##Migratsiyalarni bajarish:
python3 manage.py migrate  

##Serverni ishga tushirish:
python3 manage.py runserver 0.0.0.0:8000  


