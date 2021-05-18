from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    gender = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    phoneNumber = models.CharField(max_length=50)
    age = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    address = models.CharField(max_length=100)
    cnic = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    total_balance = models.DecimalField(max_digits=5, decimal_places=1)
    overdue = models.DecimalField(max_digits=5, decimal_places=1)


class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)


class Driver(models.Model):
    id = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    plateNum = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    seats = models.IntegerField()
    currentlocation = models.CharField(max_length=45, null=True)
    destination = models.CharField(max_length=45, null=True)
    lata = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    longa = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    latb = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    longb = models.DecimalField(max_digits=10, decimal_places=6, null=True)


class Ride(models.Model):
    rider = models.CharField(max_length=30)
    currentlocation = models.CharField(max_length=45)
    destination = models.CharField(max_length=45)
    lata = models.DecimalField(max_digits=10, decimal_places=6)
    longa = models.DecimalField(max_digits=10, decimal_places=6)
    latb = models.DecimalField(max_digits=10, decimal_places=6)
    longb = models.DecimalField(max_digits=10, decimal_places=6)
    driver = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=30)
