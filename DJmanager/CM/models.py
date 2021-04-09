from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
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


class Location(models.Model):
    name = models.CharField(max_length=50)
    xcoordinate = models.DecimalField(max_digits=5, decimal_places=3)
    ycoordinate = models.DecimalField(max_digits=5, decimal_places=3)


class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE)


class Driver(models.Model):
    username = models.OneToOneField(
        User, on_delete=models.CASCADE)
    plateNum = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    seats = models.IntegerField()


class Ride(models.Model):
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE)
    startTime = models.TimeField()
    endTime = models.TimeField()
    pickup = models.CharField(max_length=50)
    passengercount = models.IntegerField()
    totalFare = models.DecimalField(max_digits=5, decimal_places=1)
    dropoff = models.CharField(max_length=50)
    date = models.DateTimeField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    passengers = models.ManyToManyField(User)
