from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ( 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    list_filter = ("customer_id",)
    search_fields = ['customer_id', 'first_name', 'last_name', 'email']

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'enrollment_date')
    #list_filter = ("company_name",)
    search_fields = ['company_name']

@admin.register(Parkinglog)
class ParkingLogsAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'plate_number', 'subscription', 'parked')
    list_filter = ('customer_id','plate_number')
    search_fields = ['customer_id','plate_number','parked', 'user']

@admin.register(Subscriptions)
class ParkingLogsAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'plate_number', 'end_date', 'user')
    list_filter = ('customer_id','plate_number')
    search_fields = ['customer_id','plate_number', 'end_date', 'user']