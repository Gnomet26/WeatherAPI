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
Quyidagi buyruqlarni ketma-ket terminalga yozib, loyihani ishga tushiring:

```bash
git clone <repository_url>
cd WeatherAPI
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# Windows uchun: venv\Scripts\activate
pip install -r requirements.txt
# PostgreSQL serverni ishga tushiring va kerakli bazani yarating
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
