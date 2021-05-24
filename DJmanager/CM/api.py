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
            drivercount = Driver.objects.filter(destination=dest).count()
            if drivercount > 0:
                super().create(request, *args, **kwargs)
                return Response(drivers.data)
            else:
                return Response({"status": "No drivers Found"}, 200)
        return Response({"Status": "Error"}, 200)

    def update(self, request, *args, **kwargs):
        ridestatus = request.data.get('status')
        if ridestatus == 'passengerconfirmed':
            super.update(request, *args, **kwargs)
            return Response({"status": "confirming driver"})
        return Response({"status": "passenger not confirmed"})


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SponsorSerializer
