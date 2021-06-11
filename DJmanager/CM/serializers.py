from django.shortcuts import redirect
from rest_framework import serializers
from CM.models import Driver, User, Ride, Sponsor
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.urls import reverse


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'password', 'email', 'phoneNumber')

    def save(self, request):
        user = User(
            email=request.data.get('email'),
            name=request.data.get('name'),
            phoneNumber=request.data.get('phoneNumber')
        )
        user.set_password(request.data.get('password'))
        user.is_active = 1
        user.save()
        return user


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'
