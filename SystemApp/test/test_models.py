from django.test import TestCase
from django.db import transaction
from DashboardApp.views import users
from SystemApp.models import *
import os

class CustomerTestCase(TestCase):
    def setUp(self):
        pass

    def test_enroll_customers(self):
        Customers.enroll_customer('Leapr Labs', 'Rugando, Kigali, Rwanda')
        Customers.enroll_customer('Makuza Peace Plaza', 'Downtown, Kigali, Rwanda')
        
        customers_obj = Customers.objects.all()

        self.assertEqual(len(customers_obj), 2)


class UserTestCase(TestCase):
    def setUp(self):
        Customers.enroll_customer('Leapr Labs', 'Rugando, Kigali, Rwanda')
        Customers.enroll_customer('Makuza Peace Plaza', 'Downtown, Kigali, Rwanda')
        
    def test_add_user(self):
        add_1 = Users.add_user(customer_id=Customers.objects.all()[0].customer_id, first_name='fname_1', last_name='lname_1', email='test_1@gmailcom', phonenum='+250783089337', password='admin123', role='Admin')
        add_2 = Users.add_user(customer_id=Customers.objects.all()[1].customer_id, first_name='fname_2', last_name='lname_2', email='admin_2@gmailcom', phonenum='+250783089337', password='admin456', role=None)
        with transaction.atomic():
            add_3 = Users.add_user(customer_id=Customers.objects.all()[0].customer_id, first_name='fname_1', last_name='lname_1', email='test_1@gmailcom', phonenum='+250783089337', password='admin123', role='Admin')
        
        users_obj = Users.objects.all()

        #test size of the users object
        self.assertEqual(len(users_obj), 2)

        #test addition 1
        self.assertEqual(add_1, (True, users_obj[0], None))

        #test addition 2 to see if user is super user
        self.assertEqual(add_2[1].is_superuser, False)

        #test addition 3 to check duplicate email
        self.assertEqual(add_3, (False, None, 'Email already exists'))


