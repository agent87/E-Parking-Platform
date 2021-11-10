# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
# import datetime
# from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4
import datetime


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


class Users(AbstractUser):
    user_id = models.SmallAutoField(primary_key=True, editable=False)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email
    
    @classmethod
    def create_user(self, email, password, customer_id, fname, lname, contact, is_admin, ):
        self.objects.create(email=email, password=password, customer_id=customer_id, fname=fname, lname=lname, contact=contact, is_admin=is_admin)
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


# class Parkinglog(models.Model):
#     ticketid = models.UUIDField(db_column='TicketId', primary_key=True)  # Field name made lowercase.
#     customerid = models.CharField(db_column='CustomerId', max_length=50)  # Field name made lowercase.
#     date = models.DateField(db_column='Date')  # Field name made lowercase.
#     platenum = models.CharField(db_column='PlateNum', max_length=50)  # Field name made lowercase.
#     entrygateid = models.CharField(db_column='EntryGateId', max_length=50)  # Field name made lowercase.
#     checkintime = models.BigIntegerField(db_column='CheckinTime')  # Field name made lowercase.
#     checkouttime = models.BigIntegerField(db_column='CheckoutTime', blank=True, null=True)  # Field name made lowercase.
#     exitgateid = models.CharField(db_column='ExitGateId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     duration = models.FloatField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
#     cash = models.FloatField(db_column='Cash', blank=True, null=True)  # Field name made lowercase.

#     @classmethod
#     def add(self, date, time, platenumber):
#         format_datetime = datetime.datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
#         self.objects.create(platenum=platenumber, 
#                             date = format_datetime.date(),
#                             ticketid = uuid4(),
#                             customerid = 'EGPCI-AAA01-0001',
#                             checkintime= format_datetime.timestamp(),
#                             entrygateid='SouthGate',
#                             status = 'Parked')
    
#     @classmethod
#     def close(self, ticketid, checkouttime, exitgateid, cash):
#         self.objects.filter(ticketid=ticketid).update(checkouttime=checkouttime, 
#                                                       exitgateid=exitgateid)
#     @classmethod
#     def delete(self, ticketid):
#         self.objects.filter(ticketid=ticketid).delete()




# class Tarrif(models.Model):
#     tarrifid = models.UUIDField(db_column='TarrifId', primary_key=True)  # Field name made lowercase.
#     customerid = models.CharField(db_column='CustomerId', max_length=50)  # Field name made lowercase.
#     fromtime = models.FloatField(db_column='FromTime', blank=True, null=True)  # Field name made lowercase.
#     totime = models.FloatField(db_column='ToTime', blank=True, null=True)  # Field name made lowercase.
#     cost = models.FloatField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
#     initiatedby = models.CharField(db_column='Initiatedby', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
#     lastupdate = models.DateField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
#     updatelog = models.CharField(db_column='UpdateLog', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     @classmethod
#     def add_tarrif(self, fromtime, totime, cost):
#         self.objects.create(
#             tarrifid = uuid4(),
#             customerid = 'EGPCI-AAA01-0001',
#             fromtime = fromtime,
#             totime = totime,
#             cost = cost,
#             date = datetime.datetime.now().date()
#         )

#     @classmethod
#     def remove_tarrif(self, tarrifid):
#         self.objects.filter(tarrifid=tarrifid).delete()


# class Subcription:
#     customerid = models.CharField(db_column='CustomerId', max_length=50)  # Field name made lowercase.
#     subscriptionid = models.CharField(db_column='SubscriptionId', max_length=50)  # Field name made lowercase.
#     platenumber = models.CharField(db_column='PlateNumber', max_length=50)  # Field name made lowercase.
#     subscription_date = models.DateField(db_column='SubscriptionDate')  # Field name made lowercase.
#     subscription_end_date = models.DateField(db_column='SubscriptionEndDate')  # Field name made lowercase.
#     subscription_type = models.CharField(db_column='SubscriptionType', max_length=50)  # Field name made lowercase.
#     subscription_status = models.CharField(db_column='SubscriptionStatus', max_length=50)  # Field name made lowercase.
#     subscription_amount = models.FloatField(db_column='SubscriptionAmount')  # Field name made lowercase.
#     contact_number = models.CharField(db_column='ContactNumber', max_length=50)  # Field name made lowercase.
#     office_location = models.CharField(db_column='OfficeLocation', max_length=50)  # Field name made lowercase.
#     parkingLot = models.CharField(db_column='ParkingLot', max_length=50)  # Field name made lowercase.



