from SystemApp import models
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import os
import psycopg2

try:
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
except:
    conn = psycopg2.connect(database="d7pibsdo79jogi",host="ec2-52-86-25-51.compute-1.amazonaws.com",port=5432,user="cccbiffnldwfkf",password="605444bcd83d702da6e7f56cb2fba0ebb74fb3db14dc5a0c1555bbfa75a357a1")

# Create your views here.
class responses:
    def login_page(request, redirect_to=None):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                return redirect(reverse('history_page'))
            else:
                return render(request, 'DashboardApp/login.html', {'code': 302})
        else:
            return render(request, 'DashboardApp/login.html')

    
    def testing(request):
        return render(request, 'Auth/histor.html')

    #login_required
    def dashboard_page(request):
        #context = engine.ParkingLog.compile('EGPCI-AAA01-0001')

        return render(request, 'DashboardApp/dashboard.html')

    #login_required
    def history_page(request):
        #context = engine.ParkingLog.compile('EGPCI-AAA01-0001')['History']
        return render(request, 'DashboardApp/history.html')

    #login_required
    def pricing_page(request):
        context = {'tarrifs' : models.Tarrif.objects.all()}
        return render(request, 'DashboardApp/pricing.html', context)

    #login_required
    def close_ticket(request, ticketid):
        ticket = models.Parkinglog.objects.get(ticketid=ticketid)
        print(ticket)

        return redirect(reverse('parked_page'))


    #login_required
    def parked_page(request):
        parked_vehicles = models.Parkinglog.objects.filter(customer_id='EPMS-0001', status='Parked')
        return render(request, 'DashboardApp/parked.html', context={'parked_vehicles': parked_vehicles})

    #login_required
    def subscribers_page(request):
        print(request.user.customer_id.customer_id)
        context = {"subscription" : models.Subscriptions.objects.filter(customer_id = request.user.customer_id.customer_id)}
        return render(request, 'DashboardApp/subscription.html', context)

    #login_required
    def user_page(request):
        context = {'users': models.Users.objects.filter(customer_id = 'EPMS-0001')}
        return render(request, 'DashboardApp/user.html', context)

    #login_required
    def logout_request(request):
        logout(request)
        return redirect(reverse('logout_request'))

class authentication:
    def login(request):
        if request.method == "POST":
            email = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('dashboard_page'))
            else:
                return redirect(reverse('LoginView'))
        else:
            return redirect(reverse('LoginView'))

class LoginView:
    def LoginView(request):
        return render(request, 'DashboardApp/login.html')


class history:
    #login_required
    def history_page(request):
        context = {'history': models.Parkinglog.objects.filter(customer_id=request.user.customer_id.customer_id)}
        return render(request, 'DashboardApp/history.html', context)

    #login_required
    def add_ticket(request):
        if request.method == "POST":
            customer_id = request.user.customer_id.customer_id
            date = request.POST.get('date')            
            time = request.POST.get('time')
            platenumber = request.POST.get('platenumber')
            models.Parkinglog.add(customer_id, date, time, platenumber, checkin_method='Manual')
            return redirect(reverse('parked_page'))
        else:
            return(reverse('parked_page'))

    #login_required
    def close_ticket(request, ticket_id):
        pass

    
class pricing:
    #login_required
    def add_pricing(request):
        if request.method == "POST":
            customer_id = request.user.customer_id.customer_id
            fromtime = request.POST.get('fromtime')            
            totime = request.POST.get('totime')
            cost = request.POST.get('cost')
            models.Tarrif.add_tarrif(customer_id, fromtime, totime, cost)
            return redirect(reverse('pricing_page'))
        else:
            return(reverse('pricing_page'))

    #login_required
    def edit_pricing(request):
        pass

    #login_required
    def delete_pricing(request):
        pass

class users:
    @login_required
    def add_user(request):
        if request.method == "POST":
            customer_id = request.user.customer_id.customer_id
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phonenum = request.POST.get('phonenum')
            password = request.POST.get('password')
            role = request.POST.get('role')
            models.Users.add_user(customer_id, first_name, last_name, email, phonenum, password, role)
            return redirect(reverse('user_page'))
        else:
            return redirect(reverse('user_page'))

class subscription:
    @login_required
    def add_subscription(request):
        if request.method == "POST":
            customer_id = request.user.customer_id.customer_id
            platenum = request.POST.get('platenum')
            name = request.POST.get('name')
            phonenum = request.POST.get('phonenum')
            office = request.POST.get('office')
            parklot = request.POST.get('parklot')
            amount = request.POST.get('amount')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            models.Subscriptions.add_subscription(customer_id, platenum, name, phonenum, office, parklot, amount, start_date, end_date)
            return redirect(reverse('subscribers_page'))
        else:
            return redirect(reverse('subscribers_page'))