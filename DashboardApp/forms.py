from django import forms
from django.utils import timezone
import SystemApp
from .models import *
import datetime


class LoginForm(forms.Form):
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'id':'email', 'placeholder':'Email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id':'password', 'placeholder':'Password'}))
    


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

    def verify_mail(self):
        pass

class TarrifForm(forms.Form):
    tarrif_id = forms.CharField(widget = forms.HiddenInput(attrs={'id':'TarriffForm-tarrif_id'}), required = False)
    from_time = forms.IntegerField(label='From Time', widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'from_time','type':'number','placeholder':'Minutes'}))
    to_time = forms.IntegerField(label='To Time', widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'to_time', 'type':'number', 'placeholder':'Minutes'}))
    duration = forms.CharField(label='Duration', required=False, disabled=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'duration', 'placeholder':'Days/Hours/Minutes'}))
    cost = forms.IntegerField(label='Price in Rwf', widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'cost', 'type':'number', 'placeholder':'RWF'}))

    def create(self):
        tarrif = SystemApp.models.Tarrif(customer_id=self.cleaned_data['customer_id'], from_time=self.cleaned_data['from_time'], to_time=self.cleaned_data['to_time'], cost=float(self.cleaned_data['cost']), datetime=timezone.now())
        tarrif.save()
        return tarrif

    def update(self):
        tarrif = SystemApp.models.Tarrif.objects.get(pk=self.cleaned_data['tarrif_id'])
        tarrif.from_time = self.cleaned_data['from_time']
        tarrif.to_time = self.cleaned_data['to_time']
        tarrif.cost = float(self.cleaned_data['cost'])
        tarrif.save()
        return tarrif

class TicketForm:
    class CheckinForm(forms.Form):
        gate = forms.ChoiceField(label='Gate', choices=SystemApp.models.Gates.objects.all().values_list('gate_id', 'name'))
        plate_number = forms.CharField(label='Plate Number', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'plate_number', 'placeholder':'Plate Number'}))
        entry_time = forms.DateTimeField(label='Entry Time', widget=forms.DateTimeInput(attrs={'class': 'form-control', 'id':'entry_time', 'placeholder':'Entry Time'}))

        def create(self):
            pass

    class CheckoutForm(forms.Form):
        pass