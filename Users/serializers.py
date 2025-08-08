from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .utils import validate_serilizers_data

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            "username":{"validators":[]},
        }

    def validate(self, attrs):
        result = str(validate_serilizers_data(attrs=attrs))
        db_username = CustomUser.objects.filter(username = attrs.get('username')).exists()

        if result != 'Test Ok':
            raise serializers.ValidationError({"error":result})

        if db_username:
            raise serializers.ValidationError({"error":"Ushbu username foydalanuvchisi ro`yxatda mavjud"})

        return attrs

    def create(self, validated_data):

        return CustomUser.objects.create(**validated_data)


class LoginSerializer(TokenObtainPairSerializer):
    username_field = 'username'

    def validate(self, attrs):

        username = attrs.get('username')
        password = attrs.get('password')
        user = CustomUser.objects.filter(username = username).first()

        if user != None:
            if user.check_password(password):
                jwt_token = self.get_token(user = user)

                attrs['access'] = str(jwt_token.access_token)
                attrs['refresh'] = str(jwt_token)
                return attrs

            raise serializers.ValidationError({"error":"Username yoki parol xato, qaytadan urunib ko`ring"})
        raise serializers.ValidationError({"error":"Username yoki parol xato, qaytadan urunib ko`ring"})

class RefreshTokenSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        try:
            RefreshToken(attrs['refresh'])
        except:

            raise serializers.ValidationError({"error":"Token yaroqsiz yoki eskirgan"})
        data = super().validate(attrs)
        return data

class LogoutSerializer(serializers.Serializer):

    refresh = serializers.CharField()

    def validate(self, attrs):

        self.refresh = attrs.get('refresh')

        return attrs

    def save(self, **kwargs):

        try:
            token = RefreshToken(self.refresh)
            token.blacklist()
        except:

            raise serializers.ValidationError({"error":"Token yaroqsiz yoki eskirgan"})
