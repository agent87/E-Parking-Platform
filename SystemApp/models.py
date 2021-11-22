from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.hashers import make_password
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from uuid import uuid4
import time
import datetime


from .managers import CustomUserManager


class Customers(models.Model):
    customer_id = models.CharField(db_column='CustomerId', primary_key=True, max_length=50, editable=False)
    #administrator = models.ForeignKey('Users', on_delete=models.CASCADE, blank=True, null=True) 
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

    @property
    def total_entries(self):
        return Parkinglog.objects.filter(checkin_user=self.user_id).count()

    @property
    def total_entries_today(self):
        return Parkinglog.objects.filter(checkin_user = self.user_id, date_created__date=datetime.date.today()).count()

    @property
    def total_entries_this_month(self):
        return Parkinglog.objects.filter(checkin_user=self.user_id, date_created__month=datetime.date.today().month).count()

    @property
    def total_exits(self):
        return Parkinglog.objects.filter(checkout_user=self.user_id).count()

    @property
    def total_exits_today(self):
        return Parkinglog.objects.filter(checkout_user=self.user_id, exit_time__date=datetime.date.today()).count()

    @property
    def total_subscriptions(self):
        return Subscriptions.objects.filter(user=self.user_id).count()
        

    @property
    def full_names(self):
        return self.first_name + ' ' + self.last_name
        


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


class Tarrif(models.Model):
    tarrif_id = models.UUIDField(db_column='TarrifId', primary_key=True)  
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=50)
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
        return self.objects.filter(fromtime__lte=duration, totime__gte=duration).first()



    @classmethod
    def remove_tarrif(self, tarrifid):
        self.objects.filter(tarrifid=tarrifid).delete()


class Subscriptions(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(db_column='Date', blank=True, null=True)
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
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'Subscriptions'

    @classmethod
    def add_subscription(self, user_id, customer_id, platenum, name, phonenum, office, parklot, amount, start_date, end_date):
        self.objects.create(
            customer_id = Customers.objects.get(customer_id=customer_id),
            date = datetime.datetime.now().date(),
            plate_number = platenum,
            start_date = start_date,
            end_date = end_date,
            type = type,
            amount = amount,
            name = name,
            phone_number = phonenum,
            office = office,
            parklot = parklot,
            user = User.objects.get(user_id = user_id)
        )

    @classmethod
    def is_subscribed(self, plate_number):
        try:
            return self.objects.get(plate_number=plate_number, end_date__gte=datetime.datetime.now())
        except self.DoesNotExist:
            return None

    @property
    def format_end_date(self):
        return datetime.datetime.strftime(self.end_date, '%m/%d/%Y')

    @property
    def format_end_date(self):
        return datetime.datetime.strftime(self.end_date, '%m/%d/%Y')

    @classmethod
    def remove_subscription(self, subscription_id):
        self.objects.filter(subscription_id=subscription_id).delete()

    @property
    def count(self):
        self.objects.count()



class Parkinglog(models.Model):
    ticket_id = models.UUIDField(db_column='TicketId', primary_key=True)  
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(db_column='Date')  
    plate_number = models.CharField(db_column='PlateNum', max_length=50)  
    entry_gate = models.ForeignKey(Gates, related_name='entry_gate', on_delete=models.CASCADE, blank=True, null=True)  
    checkin_method = models.CharField(db_column='CheckInMethod', max_length=10)
    checkin_time = models.BigIntegerField(db_column='CheckinTime')  
    checkin_user = models.ForeignKey(Users, related_name='checkin_user', on_delete=models.CASCADE, blank=True, null=True)
    checkout_time = models.BigIntegerField(db_column='CheckoutTime', blank=True, null=True)  
    exit_gate = models.ForeignKey(Gates, related_name='exit_gate', on_delete=models.CASCADE, blank=True, null=True)  
    parked = models.BooleanField(db_column='Parked', blank=True, null=True) 
    duration = models.BigIntegerField(db_column='Duration', blank=True, null=True)  
    cost = models.BigIntegerField(db_column='Cost', blank=True, null=True)  
    amount_payed = models.BigIntegerField(db_column='AmountPayed', blank=True, null=True)
    subscription = models.ForeignKey(Subscriptions, on_delete=models.CASCADE, blank=True, null=True)  
    checkout_method = models.CharField(db_column='CheckoutMethod', max_length=10, blank=True, null=True)
    payment_method = models.CharField(db_column='PaymentMethod', max_length=50, blank=True, null=True)
    checkout_user = models.ForeignKey(Users, related_name='checkout_user', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'ParkingLog'

    @classmethod
    def add(self, customer_id, date, time, plate_number, gate_id, user_id, checkin_method):
        ticket_id = uuid4()
        format_datetime = datetime.datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
        self.objects.create(plate_number=plate_number, 
                            date = datetime.datetime.now(),
                            ticket_id = ticket_id,
                            customer_id = Customers.objects.get(customer_id=customer_id),
                            checkin_time= format_datetime.timestamp(),
                            checkin_method = checkin_method,
                            checkin_user = Users.objects.get(user_id=user_id),
                            entry_gate= Gates.objects.get(gate_id=gate_id),
                            parked = True)
        
        try:
            self.objects.filter(ticket_id=ticket_id).update(subscription=Subscriptions.objects.get(plate_number=plate_number))
        except ObjectDoesNotExist:
            pass
        
        return ticket_id
            
    
    @staticmethod
    def close(ticket_id, checkin_time, checkout_time, checkout_method, checkout_user, exit_gate, amount_payed, payment_method, *subscription):
        checkin_unix_time = datetime.datetime.strptime(checkin_time, '%m/%d/%Y %H:%M')
        checkout_unix_time = datetime.datetime.strptime(checkout_time, '%m/%d/%Y %H:%M')
        Parkinglog.objects.filter(ticket_id=ticket_id).update(
            checkin_time = checkin_unix_time.timestamp(),
            checkout_time = checkout_unix_time.timestamp(),
            checkout_method = checkout_method,
            checkout_user = Users.objects.get(user_id=checkout_user),
            exit_gate = Gates.objects.get(gate_id=exit_gate),
            cost = Tarrif.match_tarrif((checkout_unix_time - checkin_unix_time).seconds/60).cost,
            duration = (checkout_unix_time - checkin_unix_time).seconds,
            amount_payed = amount_payed,
            payment_method = payment_method,
            parked = False
        )

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
            return abs(elapsed_minutes)

    @property
    def format_duration(self):
        if self.duration:
            return round(self.duration/60)
        else:
            return None
     
    #Yep it's specially crafted function for checkout form check in field( Read it slow G/Don't get it twisted)
    #such an egoistical input right!
    @property
    def format_checkin_datetime(self):
        return datetime.datetime.fromtimestamp(self.checkin_time).strftime('%m/%d/%Y %H:%M')

    @property
    def checkin_datetime(self):
        print(datetime.datetime.fromtimestamp(self.checkin_time).strftime("%m/%d/%Y %H:%M"))
        return datetime.datetime.fromtimestamp(self.checkin_time).strftime("%m/%d/%Y %H:%M")

    @property
    def checkout_datetime(self):
        return datetime.datetime.fromtimestamp(self.checkout_time).strftime("%m/%d/%Y %H:%M")
 
    ###################### Dashboard Properties ##############################
    @property
    #todays total cars
    def todays_total_cars(self):
        return self.objects.filter(date=datetime.date.today()).count()

    @property
    def total_revenue(self):
        revenue = 0
        for log in self.objects.all():
            revenue += log.amount_payed
        return revenue
    
    @property
    def total_parked(self):
        return Parkinglog.objects.filter(parked=True).count()

    @property
    #todays revenue
    def todays_revenue(self):
        todays_revenue = 0
        for logs in Parkinglog.objects.filter(date=datetime.date.today()):
            todays_revenue += logs.amount_payed
        return todays_revenue

    #Total revenue last week
    @property
    def last_week_revenue(self):
        last_week_revenue = 0
        for logs in Parkinglog.objects.filter(date__range=[datetime.date.today() - datetime.timedelta(days=7), datetime.date.today()]):
            last_week_revenue += logs.amount_payed
        return last_week_revenue
