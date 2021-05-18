from CM.models import Driver, User, Sponsor, Ride
from rest_framework import viewsets, permissions
from .serializers import DriverSerializer, UserSerializer, SponsorSerializer, RideSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DriverSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RideSerializer

    def create(self, request, *args, **kwargs):
        ridestatus = request.data.get('status')
        if ridestatus == 'pending':
            dest = request.data.get('destination')
            drivers = DriverSerializer(
                Driver.objects.filter(destination=dest), many=True)
            super().create(request, *args, **kwargs)
            return Response(drivers.data)
        return Response({"Status": "Error"}, 200)


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SponsorSerializer
