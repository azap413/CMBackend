from CM.models import Driver, User, Sponsor, Ride
from rest_framework import viewsets, permissions
from .serializers import DriverSerializer, UserSerializer, SponsorSerializer, RideSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
import socket
from rest_framework.permissions import IsAuthenticated


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

    def perform_update(self, serializer):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ipobj = x_forwarded_for.split(',')[0]
        else:
            ipobj = self.request.META.get('REMOTE_ADDR')
        try:
            socket.inet_aton(ipobj)
            ip_valid = True
        except socket.error:
            ip_valid = False

        if serializer.is_valid() and ip_valid:
            serializer.save(ipaddr=ipobj)
        else:
            return Response({"Valid": "Not valid"})


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RideSerializer
    users = User.objects.all()

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

    def perform_update(self, serializer):
        ridestatus = self.request.data.get('status')
        if ridestatus == 'passenger confirmed':
            driverid = self.request.data.get('driver')
            # send notification here
            serializer.save(driver=driverid)
        elif ridestatus == 'driver confirmed':
            namepass = self.request.data.get('rider')
            passenger = User.objects.filter(name=namepass)
            # send notification here
            serializer.save()


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SponsorSerializer
