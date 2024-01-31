from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (RegisterSerializer, UserLoginSerializer,
                          UserSerializer)


class LoginView(APIView):
    def post(self,request):
        user_serializer=UserLoginSerializer(data=request.data)
        if not user_serializer.is_valid(raise_exception=True):
            return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        return Response(user_serializer.data,status=status.HTTP_200_OK)

    

class RegisterUserView(APIView):
    def post(self,request):
        user_serializer=RegisterSerializer(data=request.data)
        if not user_serializer.is_valid():
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user_data=user_serializer.save()
        user_serializer=UserSerializer(user_data)
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

        
    
class RestrictedView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        return Response({"response":"You are allowed here."})