from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    
    password2=serializers.CharField(write_only=True,required=True)
    email=serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    
    class Meta:
        model=CustomUser
        fields=('id','username','email','password','password2','bio','cover_photo')

    def validate(self, attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError(
                {"password":"Password fields didn't match."}
            )
        return attrs
    
    def create(self,validated_data):
        user=CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            bio=validated_data['bio'],
            cover_photo=validated_data['cover_photo']
        )
        # set the hashed password
        user.set_password(validated_data['password'])
        user.save()
        
        return user
    
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        # fields='__all__'
        model=CustomUser
        exclude=['password']
        

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token=super().get_token(user)

        token['username']=user.username
        token['email']=user.email
        
        return token
    

class UserLoginSerializer(serializers.Serializer):
    email=serializers.CharField()
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])

    # access_token=serializers.SerializerMethodField()
    # refresh_token=serializers.SerializerMethodField()


    # def get_access_token(self,obj):
    #     refresh=RefreshToken.for_user(obj)
        
    def validate(self,data):
        email=data.get('email')
        password=data.get('password')
        
        if not(email and password):
            raise serializers.ValidationError("Both fields are required")
        
        user=authenticate(username=email,password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials.")
        
        if not user.is_active:
            raise serializers.ValidationError("User account is not active.")
        
        refresh=RefreshToken.for_user(user)

        # {'refresh':str(refresh),'access':str(refresh.access_token)}
        user_data=UserSerializer(user).data
        return {
                'user': user,
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token)
            }

        # TODO try to implement the same using the SerializerMethodField() with the get prefix

    def to_representation(self,obj):
        return{
            'user':UserSerializer(obj['user']).data,
            'refresh_token': obj['refresh_token'],
            'access_token': obj['access_token']
        }