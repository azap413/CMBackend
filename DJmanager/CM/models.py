from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, name, email, password, phoneNumber, **otherfields):
        otherfields.setdefault('is_staff', True)
        otherfields.setdefault('is_superuser', True)
        otherfields.setdefault('is_active', True)
        return self.create_user(name, email, password, phoneNumber, **otherfields)

    def create_user(self, name, email, password, phoneNumber, **otherfields):
        email = self.normalize_email(email)
        user = self.model(email=email, name=name,
                          phoneNumber=phoneNumber, **otherfields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True)
    total_balance = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True,null=True)
    overdue = models.DecimalField(max_digits=5, decimal_places=1, blank=True,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phoneNumber', 'name']

    objects = CustomAccountManager()

    def __str__(self):
        return self.email


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
    lata = models.DecimalField(max_digits=50, decimal_places=20, null=True)
    longa = models.DecimalField(max_digits=50, decimal_places=20, null=True)
    latb = models.DecimalField(max_digits=50, decimal_places=20, null=True)
    longb = models.DecimalField(max_digits=50, decimal_places=20, null=True)


class Ride(models.Model):
    rider = models.CharField(max_length=30)
    currentlocation = models.CharField(max_length=45,null=True)
    destination = models.CharField(max_length=45,null=True)
    lata = models.DecimalField(max_digits=50, decimal_places=20)
    longa = models.DecimalField(max_digits=50, decimal_places=20)
    latb = models.DecimalField(max_digits=50, decimal_places=20,null=True)
    longb = models.DecimalField(max_digits=50, decimal_places=20,null=True)
    driver = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=30)
