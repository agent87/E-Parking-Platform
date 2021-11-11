from django.contrib.auth.models import AbstractUser
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

    def __str__(self):
        return self.email
    
    @classmethod
    def add_user(self, first_name, last_name, email, phonenum, password, role):
        self.objects.create(email=email, 
                            password=password, 
                            customer_id=Customers.objects.get(customer_id='EPMS-0001'), 
                            first_name=first_name, 
                            last_name=last_name, 
                            role = role,
                            phonenum=phonenum)
        return self.objects.get(email=email)

    @classmethod
    def create_admin(self, email, password, customer_id, fname, lname, contact):
        self.objects.create(email=email, password=password, customer_id=customer_id, fname=fname, lname=lname, contact=contact, is_superuser=1)
        return self.objects.get(email=email)
        


# class Cameradef(models.Model):
#     cameraid = models.CharField(db_column='CameraId', max_length=50)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.
#     modelnum = models.CharField(db_column='ModelNum', max_length=50)  # Field name made lowercase.
#     ipaddress = models.CharField(db_column='IpAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     macaddress = models.CharField(db_column='MacAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     manufacturer = models.CharField(db_column='Manufacturer', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     origin = models.CharField(db_column='Origin', max_length=50, blank=True, null=True)  # Field name made lowercase.




# class Gatesdef(models.Model):
#     gateid = models.CharField(db_column='GateId', max_length=50)  # Field name made lowercase.
#     customerid = models.CharField(db_column='CustomerId', max_length=50)  # Field name made lowercase.
#     flow = models.CharField(db_column='Flow', max_length=50)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cashiername = models.CharField(db_column='CashierName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cameraid = models.CharField(db_column='CameraId', max_length=50, blank=True, null=True)  # Field name made lowercase.


class Parkinglog(models.Model):
    ticket_id = models.UUIDField(db_column='TicketId', primary_key=True)  # Field name made lowercase.
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    platenum = models.CharField(db_column='PlateNum', max_length=50)  # Field name made lowercase.
    entrygateid = models.CharField(db_column='EntryGateId', max_length=50)  # Field name made lowercase.
    checkintime = models.BigIntegerField(db_column='CheckinTime')  # Field name made lowercase.
    checkouttime = models.BigIntegerField(db_column='CheckoutTime', blank=True, null=True)  # Field name made lowercase.
    exitgateid = models.CharField(db_column='ExitGateId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    duration = models.FloatField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    cash = models.FloatField(db_column='Cash', blank=True, null=True)  # Field name made lowercase.
    subcription_id = models.CharField(db_column='SubcriptionId', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ParkingLog'

    @classmethod
    def add(self, date, time, platenumber):
        format_datetime = datetime.datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
        self.objects.create(platenum=platenumber, 
                            date = format_datetime.date(),
                            ticket_id = uuid4(),
                            customer_id = Customers.objects.get(customer_id='EPMS-0001'),
                            checkintime= format_datetime.timestamp(),
                            entrygateid='SouthGate',
                            status = 'Parked')
    
    @classmethod
    def close(self, ticket_id, checkouttime, exitgateid, cash):
        self.objects.filter(ticket_id=ticket_id).update(checkouttime=checkouttime, 
                                                      exitgateid=exitgateid)
    @classmethod
    def delete(self, ticket_id):
        self.objects.filter(ticket_id=ticket_id).delete()

    @property
    def elapsed(self):
        if self.checkintime:
            return time.time() - self.checkintime
        
    @property
    def format_checkintime(self):
        return datetime.datetime.fromtimestamp(self.checkintime).strftime('%H:%M:%S')


class Tarrif(models.Model):
    tarrif_id = models.UUIDField(db_column='TarrifId', primary_key=True)  # Field name made lowercase.
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    fromtime = models.FloatField(db_column='FromTime', blank=True, null=True)  # Field name made lowercase.
    totime = models.FloatField(db_column='ToTime', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    initiatedby = models.CharField(db_column='Initiatedby', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    updatelog = models.CharField(db_column='UpdateLog', max_length=50, blank=True, null=True)  # Field name made lowercase.

    @classmethod
    def add_tarrif(self, fromtime, totime, cost):
        self.objects.create(
            tarrif_id = uuid4(),
            customer_id = Customers.objects.get(customer_id='EPMS-0001'),
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


class Subcription:
    customer_id = models.CharField(db_column='CustomerId', max_length=50)  # Field name made lowercase.
    subscription_id = models.CharField(db_column='SubscriptionId', max_length=50)  # Field name made lowercase.
    platenumber = models.CharField(db_column='PlateNumber', max_length=50)  # Field name made lowercase.
    subscription_date = models.DateField(db_column='SubscriptionDate')  # Field name made lowercase.
    subscription_end_date = models.DateField(db_column='SubscriptionEndDate')  # Field name made lowercase.
    subscription_type = models.CharField(db_column='SubscriptionType', max_length=50)  # Field name made lowercase.
    subscription_status = models.CharField(db_column='SubscriptionStatus', max_length=50)  # Field name made lowercase.
    subscription_amount = models.FloatField(db_column='SubscriptionAmount')  # Field name made lowercase.
    contact_number = models.CharField(db_column='ContactNumber', max_length=50)  # Field name made lowercase.
    office_location = models.CharField(db_column='OfficeLocation', max_length=50)  # Field name made lowercase.
    parkingLot = models.CharField(db_column='ParkingLot', max_length=50)  # Field name made lowercase.
