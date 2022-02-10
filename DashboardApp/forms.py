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
            gates = SystemApp.models.Gates.objects.filter(customer_id=customer_id)
            self.fields['gate'].queryset = gates
            self.gates = len(gates)
            


        def create(self):
            format_datetime = datetime.datetime.strptime(str(self.cleaned_data['date']) + ' ' + str(self.cleaned_data['entry_time']), '%Y-%m-%d %H:%M:%S') 
            ticket = SystemApp.models.Parkinglog(plate_number=self.cleaned_data['plate_number'].upper(), date = timezone.now(), customer_id = self.cleaned_data['user'].customer_id, checkin_time= format_datetime.timestamp(),checkin_method = 'Manual', checkin_user = self.cleaned_data['user'], entry_gate= SystemApp.models.Gates.objects.get(gate_id=self.cleaned_data['gate'].gate_id), parked = True)
            ticket.save()
            return ticket

    class CheckoutForm(forms.Form):
        #ticket details
        action = forms.CharField(widget = forms.HiddenInput(attrs={'id':'CheckoutForm-action'}), initial="update", required = False)
        ticket_id = forms.CharField(widget = forms.HiddenInput(attrs={'id':'CheckoutForm-ticket_id'}), required = False)
        
        show_ticket = forms.CharField(label='Ticket ID', disabled=True, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'CheckoutForm-ticket', 'placeholder':'Ticket ID'}))
        plate_number = forms.CharField(label='Plate Number', initial="", required=False, disabled=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'CheckoutForm-plate_number', 'placeholder':'Plate Number'}))
        Subscription_id  = forms.CharField(label='Subscription', required=False, disabled=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'CheckoutForm-subscription_id', 'placeholder':'Subscription'}))

        #entry details
        entry_date = forms.DateField(label='Entry Date', widget=forms.DateInput(attrs={'class': 'form-control', 'id':'checkout_entry_date', 'type':'date'}))
        entry_time = forms.TimeField(label='Entry Time', widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'time', 'id':'checkout_entry_time', 'placeholder':'Entry Time'}))
        entry_gate = forms.ModelChoiceField(label='Exit Gate', queryset=SystemApp.models.Gates.objects.all(), initial=0, widget=forms.Select(attrs={'class': 'form-control', 'id':'checkout_entry_gate'}))
        
        #exit details
        exit_date = forms.DateField(label='Exit Date', widget=forms.DateInput(attrs={'class': 'form-control', 'id':'checkout_exit_date', 'type':'date'}))
        exit_time = forms.TimeField(label='Exit Time', widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'time', 'id':'checkout_exit_time', 'placeholder':'Entry Time'}))
        exit_gate = forms.ModelChoiceField(label='Exit Gate', queryset=SystemApp.models.Gates.objects.all(), initial=0, widget=forms.Select(attrs={'class': 'form-control', 'id':'checkout_exit_gate'}))
        
        #payment detials
        Mobile_Money = "Mobile Money"
        Cash = "Cash"
        Cheque = "Cheque"
        Bank_Transfer = "Bank Transfer"
        Debit_Card = "Visa Card"
        Ewawe_Card = "Ewawe Card"   
        Subscription = "Subscription"
        Payment_Method = (
                (Mobile_Money, 'Mobile Money'),
                (Cash, 'Cash'),
                (Cheque, 'Cheque'),
                (Bank_Transfer, 'Bank Transfer'),
                (Debit_Card, 'Debit Card'),
                (Ewawe_Card, 'Ewawe Card'),
                (Subscription, 'Subscription'),
            )
        cost = forms.IntegerField(label='Cost', disabled=True, required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'checkout_cost', 'placeholder':'Cost'}))
        payed = forms.IntegerField(label='Amount Payed', widget=forms.NumberInput(attrs={'class': 'form-control', 'value':0, 'id':'checkout_amount_payed', 'placeholder':'Amount Payed'}))
        method = forms.CharField(label='Payment Method', widget=forms.Select(choices=Payment_Method, attrs={'class': 'form-control', 'id':'checkout_payment_method'}))


        def update(self):
            ticket = SystemApp.models.Parkinglog.objects.get(ticket_id=self.cleaned_data['ticket_id'])
            ticket.checkout_time = datetime.datetime.strptime(str(self.cleaned_data['exit_date']) + ' ' + str(self.cleaned_data['exit_time']), '%Y-%m-%d %H:%M:%S').timestamp()
            ticket.checkout_gate = SystemApp.models.Gates.objects.get(gate_id=self.cleaned_data['exit_gate'].gate_id)
            ticket.checkout_method = 'Manual'
            ticket.exit_gate = SystemApp.models.Gates.objects.get(gate_id=self.cleaned_data['exit_gate'].gate_id)
            ticket.checkout_user = self.cleaned_data['user']
            ticket.amount_payed = self.cleaned_data['payed']
            ticket.payment_method = self.cleaned_data['method']
            ticket.parked = False
            ticket.save()
            print("----------------done---------------")
            return ticket

class SubscriptionForm(forms.ModelForm):
 
    class Meta:
        model = SystemApp.models.Subscriptions
        exclude = ['customer_id', 'subscription_id', 'user']

    def create(self, user):
        instance = SystemApp.models.Subscriptions(customer_id=user.customer_id,  user=user)
        pass

    def update(self):
        pass

    def delete(self):
        pass