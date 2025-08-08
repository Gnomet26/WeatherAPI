from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer, RefreshTokenSerializer, LogoutSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

class RegisterView(APIView):

    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Siz muvaffaqiyatli ro'yxatdan o'tdingiz.",
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):

    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            serializer_validate_data = serializer.validated_data
            response = {
                "access_token":serializer_validate_data.get('access'),
                "refresh_token":serializer_validate_data.get('refresh')
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RefreshToken_(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = RefreshTokenSerializer(data = request.data)

        if serializer.is_valid():
            all_data = serializer.validated_data

            return Response(all_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serilaizer = LogoutSerializer(data = request.data)

        if serilaizer.is_valid():
            serilaizer.save()
            return Response({"details":"Muvoffaqiyatli logout qilindingiz"},status=status.HTTP_205_RESET_CONTENT)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)
