from django import forms 
import SystemApp
from .models import *
import datetime


class LoginForm(forms.Form):
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'id':'email', 'placeholder':'Email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id':'password', 'placeholder':'Password'}))
    

class RegistrationForm:
    def __init__(self, *args, **kwargs):
        self.AdminForm = UserForm()
        self.CustomerForm = CustomerForm()

class CustomerForm(forms.Form):
    customer_name = forms.CharField(label='Company Name', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'customer_name', 'placeholder':'Company Name'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'address', 'placeholder':'Address'}))
    
class UserForm(forms.Form):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'first_name', 'placeholder':'Name'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'last_name', 'placeholder':'Last Name'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'id':'email', 'placeholder':'Email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id':'password', 'placeholder':'Password'}))
    phonenum = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'phonenum'}))

    class Meta:      
        model = SystemApp.models.Users

class TarrifForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'name', 'placeholder':'Name'}))
    from_time = forms.TimeField(label='From Time', widget=forms.TimeInput(attrs={'class': 'form-control', 'id':'from_time', 'placeholder':'From Time'}))
    to_time = forms.TimeField(label='To Time', widget=forms.TimeInput(attrs={'class': 'form-control', 'id':'to_time', 'placeholder':'To Time'}))
    price = forms.IntegerField(label='Price', widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'price', 'placeholder':'Price'}))
    date = datetime.datetime.now().date()


    