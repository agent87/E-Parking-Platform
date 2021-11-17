from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.db import models
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4
import time
import datetime

from .managers import CustomUserManager


class Customers(models.Model):
    customer_id = models.CharField(db_column='CustomerId', primary_key=True, max_length=50, editable=False)
    client_type = models.CharField(db_column='ClientType', max_length=70, blank=True, null=True) 
    administrator = models.ForeignKey('Users', on_delete=models.CASCADE, blank=True, null=True) 
    company_name = models.CharField(db_column='CompanyName', max_length=50, blank=True, null=True) 
    email = models.CharField(db_column='CompanyMail', max_length=70, blank=True, null=True) 
    contact = models.CharField(db_column='CompanyId', max_length=30, blank=True, null=True) 
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)
    geolocation = models.CharField(db_column='GeoLocation', max_length=50, blank=True, null=True)
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  
    comments = models.CharField(db_column='Comments', max_length=500, blank=True, null=True)  
    enrollment_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'Customers'

class Users(AbstractUser):
    user_id = models.SmallAutoField(primary_key=True, unique=True, editable=False)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    phonenum = models.CharField(db_column='PhoneNum', max_length=30, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'Users'

    def __str__(self):
        return self.email
    
    @classmethod
    def add_user(self, customer_id, first_name, last_name, email, phonenum, password, role):
        self.objects.create(email=email,  
                            customer_id=Customers.objects.get(customer_id=customer_id), 
                            first_name=first_name, 
                            last_name=last_name, 
                            role = role,
                            password = make_password(password),
                            phonenum=phonenum)
        
    @classmethod
    def create_admin(self, email, password, customer_id, fname, lname, contact):
        self.objects.create(email=email, password=password, customer_id=customer_id, fname=fname, lname=lname, contact=contact, is_superuser=1)
        return self.objects.get(email=email)
        


# class Cameradef(models.Model):
#     cameraid = models.CharField(db_column='CameraId', max_length=50)  
#     type = models.CharField(db_column='Type', max_length=50)  
#     modelnum = models.CharField(db_column='ModelNum', max_length=50)  
#     ipaddress = models.CharField(db_column='IpAddress', max_length=50, blank=True, null=True)  
#     macaddress = models.CharField(db_column='MacAddress', max_length=50, blank=True, null=True)  
#     manufacturer = models.CharField(db_column='Manufacturer', max_length=50, blank=True, null=True)  
#     origin = models.CharField(db_column='Origin', max_length=50, blank=True, null=True)  




class Gates(models.Model):    
    gate_id = models.AutoField(db_column='GateId', editable=False, primary_key=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=50)
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  
    camera_id = models.CharField(db_column='CameraId', max_length=50, blank=True, null=True)  
    cashiers = models.JSONField(db_column='Cashiers', blank=True, null=True)

    class Meta:
        db_table = 'Gates'


class Parkinglog(models.Model):
    ticket_id = models.UUIDField(db_column='TicketId', primary_key=True)  
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(db_column='Date')  
    plate_number = models.CharField(db_column='PlateNum', max_length=50)  
    entry_gate = models.CharField(db_column='EntryGate', max_length=50)  
    checkin_method = models.CharField(db_column='CheckInMethod', max_length=10)
    checkin_time = models.BigIntegerField(db_column='CheckinTime')  
    checkin_user = models.CharField(db_column='CheckinUser', max_length=50, blank=True, null=True)
    checkout_time = models.BigIntegerField(db_column='CheckoutTime', blank=True, null=True)  
    exit_gate = models.CharField(db_column='ExitGate', max_length=50, blank=True, null=True)  
    parked = models.BooleanField(db_column='Parked', blank=True, null=True) 
    duration = models.BigIntegerField(db_column='Duration', blank=True, null=True)  
    cash = models.FloatField(db_column='Cash', blank=True, null=True)  
    subcription = models.ForeignKey('Subscriptions', on_delete=models.CASCADE, blank=True, null=True)  
    checkout_method = models.CharField(db_column='CheckoutMethod', max_length=10, blank=True, null=True)
    payment_method = models.CharField(db_column='PaymentMethod', max_length=10, blank=True, null=True)
    checkout_user = models.CharField(db_column='CheckoutUser', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'ParkingLog'

    @classmethod
    def add(self, customer_id, date, time, platenumber, checkin_method):
        format_datetime = datetime.datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
        self.objects.create(plate_number=platenumber, 
                            date = format_datetime.date(),
                            ticket_id = uuid4(),
                            customer_id = Customers.objects.get(customer_id=customer_id),
                            checkin_time= format_datetime.timestamp(),
                            checkin_method = checkin_method,
                            entry_gate='SouthGate',
                            parked = True)
    
    @classmethod
    def close(self, ticket_id, checkout_time, exit_gate, cash, *subscription):
        ticket = self.objects.get(ticket_id=ticket_id)
        ticket.checkout_time = checkout_time
        ticket.save()
        ticket.duration = round(time.time() - ticket.checkin_time)
        ticket.save()
        ticket.parked = False
        ticket.save()
        ticket.cash = cash
        ticket.save()
        ticket.exit_gate = exit_gate
        ticket.save()
        try:
            ticket.subscription = Subscriptions.objects.get(subscription_id = subscription)
        except TypeError:
            pass
        ticket.save()

    @classmethod
    def delete(self, ticket_id):
        self.objects.filter(ticket_id=ticket_id).delete()

    # Count elapsed time in seconds between checkin and current time
    # convert to minutes
    @property
    def elapsed(self):
        if self.checkin_time:
            elapsed_seconds = time.time() - self.checkin_time
            elapsed_minutes = round(elapsed_seconds / 60)
            return elapsed_minutes

    @property
    def format_duration(self):
        if self.duration:
            return round(self.duration/60)
        else:
            return None
     
    @property
    def format_checkintime(self):
        return datetime.datetime.fromtimestamp(self.checkin_time).strftime('%H:%M')


class Tarrif(models.Model):
    tarrif_id = models.UUIDField(db_column='TarrifId', primary_key=True)  
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    fromtime = models.FloatField(db_column='FromTime', blank=True, null=True)  
    totime = models.FloatField(db_column='ToTime', blank=True, null=True)  
    cost = models.FloatField(db_column='Cost', blank=True, null=True)  
    initiatedby = models.CharField(db_column='Initiatedby', max_length=50, blank=True, null=True)  
    date = models.DateField(db_column='Date', blank=True, null=True)  
    lastupdate = models.DateField(db_column='LastUpdate', blank=True, null=True)  
    updatelog = models.CharField(db_column='UpdateLog', max_length=50, blank=True, null=True)  

    class Meta:
        db_table = 'Tarrif'

    @classmethod
    def add_tarrif(self, customer_id, fromtime, totime, cost):
        self.objects.create(
            tarrif_id = uuid4(),
            customer_id = Customers.objects.get(customer_id=customer_id),
            fromtime = fromtime,
            totime = totime,
            cost = cost,
            date = datetime.datetime.now().date()
        )

    @classmethod
    def match_tarrif(self, duration):
        return self.objects.filter(fromtime__lte=duration, totime__gte=duration)



    @classmethod
    def remove_tarrif(self, tarrifid):
        self.objects.filter(tarrifid=tarrifid).delete()


class Subscriptions(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    subscription_id = models.BigAutoField(db_column='SubscriptionId', primary_key=True)  
    plate_number = models.CharField(db_column='PlateNumber', max_length=50)  
    start_date = models.DateField(db_column='start')  
    end_date = models.DateField(db_column='end')  
    type = models.CharField(db_column='SubscriptionType', max_length=50)
    amount = models.FloatField(db_column='SubscriptionAmount')  
    name = models.CharField(db_column='Name', max_length=50)  
    phone_number = models.CharField(db_column='ContactNumber', max_length=50)  
    office = models.CharField(db_column='OfficeLocation', max_length=50)  
    parklot = models.CharField(db_column='ParkingLot', max_length=50)  

    class Meta:
        db_table = 'Subscriptions'

    @classmethod
    def add_subscription(self, customer_id, platenum, name, phonenum, office, parklot, amount, start_date, end_date):
        self.objects.create(
            customer_id = Customers.objects.get(customer_id=customer_id),
            plate_number = platenum,
            start_date = start_date,
            end_date = end_date,
            type = type,
            amount = amount,
            name = name,
            phone_number = phonenum,
            office = office,
            parklot = parklot
        )

    @classmethod
    def is_subscribed(self, plate_number):
        try:
            return self.objects.get(plate_number=plate_number, end_date__gte=datetime.datetime.now())
        except self.DoesNotExist:
            return None
