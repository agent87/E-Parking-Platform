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

    def send_mail(self):
        pass

class TarrifForm(forms.Form):
    tarrif_id = forms.CharField(widget = forms.HiddenInput(attrs={'id':'TarriffForm-tarrif_id'}), required = False)
    from_time = forms.IntegerField(label='From Time', widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'from_time','type':'number', 'min': 0,'placeholder':'Minutes'}))
    to_time = forms.IntegerField(label='To Time', widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'to_time', 'type':'number', 'min': 0,'placeholder':'Minutes'}))
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
        date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'class': 'form-control', 'id':'date', 'type':'date'}))
        entry_time = forms.TimeField(label='Entry Time', widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'time', 'id':'entry_time', 'placeholder':'Entry Time'}))
        gate = forms.ModelChoiceField(label='Gate', queryset=SystemApp.models.Gates.objects.all(), initial=0, widget=forms.Select(attrs={'class': 'form-control', 'id':'gate'}))
        plate_number = forms.CharField(label='Plate Number', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'plate_number', 'placeholder':'Plate Number' ,  'minlength':'6', 'maxlength':'7','pattern':'[a-zA-Z0-9]+'}))
        

        def populate(self, customer_id):
            form = self.fields['gate'].queryset = SystemApp.models.Gates.objects.filter(customer_id=customer_id)
            return form
            


        def create(self):
            format_datetime = datetime.datetime.strptime(str(self.cleaned_data['date']) + ' ' + str(self.cleaned_data['entry_time']), '%Y-%m-%d %H:%M:%S')
            ticket = SystemApp.models.Parkinglog(plate_number=self.cleaned_data['plate_number'].upper(), date = timezone.now(), customer_id = self.cleaned_data['user'].customer_id, checkin_time= format_datetime.timestamp(),checkin_method = 'Manual', checkin_user = self.cleaned_data['user'], entry_gate= SystemApp.models.Gates.objects.get(gate_id=self.cleaned_data['gate'].gate_id), parked = True)
            ticket.save()
            return ticket

    class CheckoutForm(forms.Form):
        ticket_id = forms.CharField(widget = forms.HiddenInput(attrs={'id':'CheckoutForm-ticket_id'}), required = False)
        action = forms.CharField(widget = forms.HiddenInput(attrs={'id':'CheckoutForm-action'}), required = False)
        class CheckinSection:
            pass
        class CheckoutSection:
            pass

class SubscriptionForm(forms.Form):
    customer_name = forms.CharField(label='Customer Name', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'customer_name', 'placeholder':'Name'}))
    plate_number = forms.CharField(label='Plate Number', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'plate_number', 'placeholder':'Plate Number' ,  'minlength':'6', 'maxlength':'7','pattern':'[a-zA-Z0-9]+'}))
    phonenum = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'phonenum'}))
    amount = forms.IntegerField(label='Price in Rwf', widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'amount', 'type':'number', 'placeholder':'RWF'}))
    start_date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'class': 'form-control', 'id':'start_date', 'type':'date'}))
    end_date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'class': 'form-control', 'id':'end_date', 'type':'date'}))

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass