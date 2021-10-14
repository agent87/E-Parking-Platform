# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cameradef(models.Model):
    cameraid = models.CharField(db_column='CameraId', max_length=50)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.
    modelnum = models.CharField(db_column='ModelNum', max_length=50)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IpAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    origin = models.CharField(db_column='Origin', max_length=50, blank=True, null=True)  # Field name made lowercase.


class Customers(models.Model):
    customerid = models.CharField(db_column='CustomerId', primary_key=True, max_length=50)  # Field name made lowercase.
    clienttype = models.CharField(db_column='ClientType', max_length=70, blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=80, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=13, blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=20, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    companymail = models.CharField(db_column='CompanyMail', max_length=70, blank=True, null=True)  # Field name made lowercase.
    companyid = models.CharField(db_column='CompanyId', max_length=30, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=50, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=40, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=30, blank=True, null=True)  # Field name made lowercase.
    geolocation = models.CharField(db_column='GeoLocation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=500, blank=True, null=True)  # Field name made lowercase.
    enrollmentdate = models.DateField(blank=True, null=True)



class Gatesdef(models.Model):
    gateid = models.CharField(db_column='GateId', max_length=50)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerId', max_length=50)  # Field name made lowercase.
    flow = models.CharField(db_column='Flow', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cashiername = models.CharField(db_column='CashierName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cameraid = models.CharField(db_column='CameraId', max_length=50, blank=True, null=True)  # Field name made lowercase.


class Parkinglog(models.Model):
    ticketid = models.UUIDField(db_column='TicketId', primary_key=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerId', max_length=50)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    platenum = models.CharField(db_column='PlateNum', max_length=50)  # Field name made lowercase.
    entrygateid = models.CharField(db_column='EntryGateId', max_length=50)  # Field name made lowercase.
    checkintime = models.BigIntegerField(db_column='CheckinTime')  # Field name made lowercase.
    checkouttime = models.BigIntegerField(db_column='CheckoutTime', blank=True, null=True)  # Field name made lowercase.
    exitgateid = models.CharField(db_column='ExitGateId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    duration = models.FloatField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    cash = models.FloatField(db_column='Cash', blank=True, null=True)  # Field name made lowercase.



class Tarrif(models.Model):
    customerid = models.CharField(db_column='CustomerId', max_length=50)  # Field name made lowercase.
    fromtime = models.FloatField(db_column='FromTime', blank=True, null=True)  # Field name made lowercase.
    totime = models.FloatField(db_column='ToTime', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    initiatedby = models.CharField(db_column='Initiatedby', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    updatelog = models.CharField(db_column='UpdateLog', max_length=50, blank=True, null=True)  # Field name made lowercase.




class Subcription:
    customerid = models.CharField(db_column='CustomerId', max_length=50)  # Field name made lowercase.
    subscriptionid = models.CharField(db_column='SubscriptionId', max_length=50)  # Field name made lowercase.
    platenumber = models.CharField(db_column='PlateNumber', max_length=50)  # Field name made lowercase.
    subscription_date = models.DateField(db_column='SubscriptionDate')  # Field name made lowercase.
    subscription_end_date = models.DateField(db_column='SubscriptionEndDate')  # Field name made lowercase.
    subscription_type = models.CharField(db_column='SubscriptionType', max_length=50)  # Field name made lowercase.
    subscription_status = models.CharField(db_column='SubscriptionStatus', max_length=50)  # Field name made lowercase.
    subscription_amount = models.FloatField(db_column='SubscriptionAmount')  # Field name made lowercase.
    contact_number = models.CharField(db_column='ContactNumber', max_length=50)  # Field name made lowercase.
    office_location = models.CharField(db_column='OfficeLocation', max_length=50)  # Field name made lowercase.
    parkingLot = models.CharField(db_column='ParkingLot', max_length=50)  # Field name made lowercase.



