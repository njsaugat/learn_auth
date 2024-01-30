from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import CustomUser

from .serializers import RegisterSerializer, UserLoginSerializer


class LoginView(APIView):
    def post(self,request):
        # email=request.data.get('email')
        # password=request.data.get('password') 
        user_serializer=UserLoginSerializer(data=request.data)
        if not user_serializer.is_valid(raise_exception=True):
            return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        # refresh=RefreshToken.for_user(user)
        return Response(user_serializer,status=status.HTTP_200_OK)




class RegisterUserView(generics.CreateAPIView):
    queryset=CustomUser.objects.all()
    permission_classes=[AllowAny]
    serializer_class=RegisterSerializer
    
class RestrictedView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        return Response({"response":"You are allowed here."})