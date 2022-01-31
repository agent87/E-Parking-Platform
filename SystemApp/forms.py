from django.forms import ModelForm
from django import forms
from .models import *


class CustomersForm(ModelForm):
    class Meta:
        model = Customers
        fields = ['company_name', 'address']
        labels = {
            'company_name': 'Company Name',
            'address': 'Address',
        }
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'})
        }


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['customer_id', 'first_name', 'last_name', 'email', 'phonenum', 'password', 'role']