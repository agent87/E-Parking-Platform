from django.forms import ModelForm
from .models import *


class CustomersForm(ModelForm):
    class Meta:
        model = Customers
        fields = ['company_name', 'address']


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['customer_id', 'first_name', 'last_name', 'email', 'phonenum', 'password', 'role']