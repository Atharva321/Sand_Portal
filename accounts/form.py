from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Customer, Dealer , Order
from django.db import models

class Order(UserCreationForm):
    CHOICES = (
        ('area1', 'zone1'),
        ('area2', 'zone2'),
        ('area3', 'zone3'),
        ('area4', 'zone4'),
        ('area5', 'zone5'),
    )
    ouser = models.CharField(max_length=20)
    sand = models.CharField(max_length=20)
    city = models.CharField(max_length=6, choices=CHOICES, default='zone1')

    class Meta(UserCreationForm.Meta):
        model = Order
    @transaction.atomic
    def save(self):
        order = super().save(commit=False)
        order.ouser = self.cleaned_data.get('ouser')
        order.sand = self.cleaned_data.get('sand')
        order.city =self.cleaned_data.get('city')




class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)
    image = forms.ImageField()


    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.image = self.cleaned_data.get('image')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.location = self.cleaned_data.get('location')
        customer.save()
        return user


class DealerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)
    image = forms.ImageField()


    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_dealer = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.image = self.cleaned_data.get('image')

        user.save()
        dealer = Dealer.objects.create(user=user)
        dealer.phone_number = self.cleaned_data.get('phone_number')
        dealer.designation = self.cleaned_data.get('designation')
        dealer.save()
        return user
