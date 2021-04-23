from django.db import models
from django.contrib.auth.models import AbstractUser

CHOICES = (
    ('area1', 'zone1'),
    ('area2', 'zone2'),
    ('area3', 'zone3'),
    ('area4', 'zone4'),
    ('area5', 'zone5'),
)

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_dealer = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', default="")


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

class Dealer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

