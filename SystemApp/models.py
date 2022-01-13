from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.hashers import make_password
from django.db import models
from django.db.models import Count, Avg, Sum, Max, Min
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from uuid import uuid4
import time
import datetime
from System import utilities


from .managers import CustomUserManager


class Customers(models.Model):
    customer_id = models.SmallAutoField(db_column='CustomerId', primary_key=True, editable=False)
    #administrator = models.ForeignKey('Users', on_delete=models.CASCADE, blank=True, null=True) 
    company_name = models.CharField(db_column='CompanyName', max_length=50, blank=True, null=True) 
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=500, blank=True, null=True)  
    enrollment_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'Customers'

    @classmethod
    def enroll_customer(self, company_name, address, comments):
        self.objects.create(company_name=company_name, address=address, comments=comments, enrollment_date=datetime.date.today())
        return True, self.objects.latest('customer_id')


    @property
    def cars_today(self):
        return Parkinglog.objects.filter(customer_id=self.customer_id, date=datetime.date.today()).count()

    @property
    def cars_total(self):
        return Parkinglog.objects.filter(customer_id=self.customer_id).count()

    @property
    def revenue_today(self):
        revenue = Parkinglog.objects.filter(customer_id=self.customer_id, date=datetime.date.today()).aggregate(Sum('cost'))['cost__sum']
        if revenue is None:
            return 0
        else:
            return "{:,.0f}".format(revenue)

    @property
    def revenue_total(self):
        revenue = Parkinglog.objects.filter(customer_id=self.customer_id).aggregate(Sum('cost'))['cost__sum']
        if revenue is None:
            return 0
        else:
            return "{:,.0f}".format(revenue)

    @property
    def revenue_this_week(self):
        revenue = Parkinglog.objects.filter(customer_id=self.customer_id, date__gte=datetime.date.today()-datetime.timedelta(days=7)).aggregate(Sum('cost'))['cost__sum']
        if revenue is None:
            return 0
        else:
            return "{:,.0f}".format(revenue)

    @property
    def cars_parked(self):
        return Parkinglog.objects.filter(customer_id=self.customer_id, parked=True).count()

    @property
    def payements_summary(self):
        payements = []
        for account in list(Parkinglog.objects.filter(customer_id=self.customer_id).order_by().values('payment_method').distinct()):
            account_summary = {'name': account['payment_method']}
            account_summary['count'] =  Parkinglog.objects.filter(customer_id=self.customer_id, payment_method=account['payment_method']).count()
            account_summary['sum'] = "{:,.0f}".format(Parkinglog.objects.filter(customer_id=self.customer_id, payment_method=account['payment_method']).aggregate(Sum('cost'))['cost__sum'])
            payements.append(account_summary)
        return payements
    

class Users(AbstractUser):
    user_id = models.SmallAutoField(primary_key=True, unique=True, editable=False)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    phonenum = models.CharField(db_column='PhoneNum', max_length=30, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    username = None
    mail_verified = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'Users'

    def __str__(self):
        return self.email
    
    @classmethod
    def add_user(self, customer_id, first_name, last_name, email, phonenum, password, role):
        try:
            is_superuser = True if role == 'Admin' else False
            mail_verification_token = utilities.mail_server.generate_mail_verification_token()
            self.objects.create(email=email,  
                            customer_id=Customers.objects.get(customer_id=customer_id), 
                            first_name=first_name, 
                            last_name=last_name, 
                            role = role,
                            is_superuser = is_superuser,
                            password = make_password(password),
                            phonenum=phonenum,
                            mail_verified=mail_verification_token)
            utilities.mail_server.send('Ewawe-parking user account verification', 
                                        f'''Hello {first_name}, 
                                        \n To continue using the platform, use the following link to verify your account.
                                        \n link : https://ewawe-parking.herokuapp.com/sign-up/verify-mail/{mail_verification_token}
                                        \n
                                        \n Thank you for using our services.
                                        \n Ewawe Parking

                                        ''',  [email])

            return True, self.objects.latest('user_id')
        except IntegrityError:
            return False, 'Email already exists'
    
    @property
    def total_entries(self):
        return Parkinglog.objects.filter(checkin_user=self.user_id).count()

    @property
    def total_entries_today(self):
        return Parkinglog.objects.filter(checkin_user = self.user_id, date_created__date=datetime.date.today()).count()

    
    @property
    def total_exits(self):
        return Parkinglog.objects.filter(checkout_user=self.user_id).count()

    @property
    def total_subscriptions(self):
        return Subscriptions.objects.filter(user=self.user_id).count()

    @property
    def subscriptions_sales(self):
        sales =  Subscriptions.objects.filter(user=self.user_id).aggregate(Sum('amount'))['amount__sum']
        if sales is None:
            return 0
        else:
            return 0

    @property
    def todays_sales(self):
        today_datetime = datetime.datetime.now()
        today_date_unix = datetime.datetime(today_datetime.year, today_datetime.month, today_datetime.day).timestamp()
        sales =  Parkinglog.objects.filter(checkin_user = self.user_id, checkout_time__gte = today_date_unix).aggregate(Sum('cost'))['cost__sum']
        if sales is None:
            return 0
        else:
            return 0

    @property
    def format_date_joined(self):
        return self.date_joined.strftime('%b %d, %Y')
        

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
    status = models.CharField(db_column='Status', max_length=50)
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  
    camera_id = models.CharField(db_column='CameraId', max_length=50, blank=True, null=True)  
    cashiers = models.JSONField(db_column='Cashiers', blank=True, null=True)

    class Meta:
        db_table = 'Gates'

    @classmethod
    def add_gate(self, customer_id, name, status, description=None, camera_id=None, cashiers=None):
        try:
            self.objects.create(customer_id=customer_id, name=name, status=status, description=description, camera_id=camera_id, cashiers=cashiers)
            return True, self.objects.latest('gate_id')
        except IntegrityError:
            return False, 'Gate name already exists'

    @property
    def total_entries(self):
        return Parkinglog.objects.filter(customer_id = self.customer_id.customer_id, entry_gate = self.gate_id).count()

    @property
    def total_exits(self):
        return Parkinglog.objects.filter(customer_id = self.customer_id.customer_id, exit_gate = self.gate_id).count()

    @property
    def traffic_ratio(self):
        try:
            return (self.total_exits / self.total_entries) * 100
        except ZeroDivisionError:
            return 0

   
class Tarrif(models.Model):
    tarrif_id = models.AutoField(db_column='TarrifId',primary_key=True)  
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
        ordering = ('fromtime','totime')


    @classmethod
    def add_tarrif(self, customer_id, fromtime, totime, cost):
        self.objects.create(
            customer_id = Customers.objects.get(customer_id=customer_id),
            fromtime = fromtime,
            totime = totime,
            cost = cost,
            date = datetime.datetime.now().date()
        )

    @classmethod
    def match_tarrif(self, duration):
        try:
            return self.objects.filter(fromtime__lte=duration, totime__gte=duration).first()
        except AttributeError:
            return 0

    @classmethod
    def remove_tarrif(self, tarrifid):
        self.objects.filter(tarrifid=tarrifid).delete()

    @property
    def fromtime_formatted(self):
        return utilities.time_str(self.fromtime * 60)

    @property
    def totime_formatted(self):
        return utilities.time_str(self.totime * 60)

    @property
    def cost_formated(self):
        return '{:,.0f}'.format(int(self.cost))

    #pyhton script to turn elapsed into verbal time


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
            user = Users.objects.get(user_id = user_id)
        )

        return True, phonenum, name, platenum, end_date, amount, Customers.objects.get(customer_id=customer_id).company_name

    @classmethod
    def is_subscribed(self, customer_id, plate_number):
        try:
            return self.objects.get(customer_id = customer_id, plate_number=plate_number, end_date__gte=datetime.datetime.now())
        except self.DoesNotExist:
            return None
        except self.MultipleObjectsReturned:
            return self.objects.filter(customer_id = customer_id, plate_number=plate_number, end_date__gte=datetime.datetime.now()).first()

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
    ticket_id = models.BigAutoField(db_column='TicketId',  primary_key=True)  
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
        ordering = ('-checkin_time',)

    @classmethod
    def add(self, customer_id, date, time, plate_number, gate_id, user_id, checkin_method):
        format_datetime = datetime.datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
        self.objects.create(plate_number=plate_number, 
                            date = datetime.datetime.now(),
                            customer_id = Customers.objects.get(customer_id=customer_id),
                            checkin_time= format_datetime.timestamp(),
                            checkin_method = checkin_method,
                            checkin_user = Users.objects.get(user_id=user_id),
                            entry_gate= Gates.objects.get(gate_id=gate_id),
                            parked = True)
        
        return self.objects.latest('ticket_id')
            
    
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
            amount_payed = int(amount_payed),
            payment_method = payment_method,
            parked = False
        )

    @classmethod
    def delete(self, ticket_id):
        self.objects.filter(ticket_id=ticket_id).delete()

    # Count elapsed time in seconds between checkin and current time
    # convert to minutes
    @property
    def format_elapsed(self):
        intervals = (
        ('weeks', 604800),  # 60 * 60 * 24 * 7
        ('days', 86400),    # 60 * 60 * 24
        ('hours', 3600),    # 60 * 60
        ('minutes', 60),
        ('seconds', 1),)

        result = []
        granularity=1
        elapsed_seconds = round(abs(time.time() - self.checkin_time))
        for name, count in intervals:
            value = round(elapsed_seconds // count)
            if value:
                elapsed_seconds -= value * count
                if value == 1:
                    name = name.rstrip('s')
                result.append("{} {}".format(value, name))
        return f'{result[0]} ago '

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
    def is_subscribed(self):
        if self.subscription != None:
            return True
        else:
            return False


def delete_customer(customer_id):
    Parkinglog.objects.filter(customer_id=customer_id).delete()
    Gates.objects.filter(customer_id=customer_id).delete()
    Users.objects.filter(customer_id=customer_id).delete()
    Subscriptions.objects.filter(customer_id=customer_id).delete()
    Tarrif.objects.filter(customer_id=customer_id).delete()
    Customers.objects.filter(customer_id=customer_id).delete()

def view_customer_users(customer_id):
    users =  Users.objects.filter(customer_id=customer_id)
    for user in users:
        print(user.email)

def view_customers():
    for customer in Customers.objects.all():
        print(customer.customer_id, customer.company_name)