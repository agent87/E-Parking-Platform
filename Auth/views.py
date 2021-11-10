from Auth import models
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import os
import psycopg2
from . import engine
from . import models

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
                return render(request, 'Auth/login.html', {'code': 302})
        else:
            return render(request, 'Auth/login.html')

    
    def testing(request):
        return render(request, 'Auth/histor.html')

    @login_required
    def dashboard_page(request):
        context = engine.ParkingLog.compile('EGPCI-AAA01-0001')

        return render(request, 'Auth/dashboard.html', context)

    @login_required
    def history_page(request):
        context = engine.ParkingLog.compile('EGPCI-AAA01-0001')['History']
        return render(request, 'Auth/history.html', context)

    @login_required
    def pricing_page(request):
        context = {'tarrifs' : models.Tarrif.objects.all()}
        return render(request, 'Auth/pricing.html', context)

    @login_required
    def close_ticket(request, ticketid):
        ticket = models.Parkinglog.objects.get(ticketid=ticketid)
        print(ticket)

        return redirect(reverse('parked_page'))


    @login_required
    def parked_page(request):
        context = engine.ParkingLog.compile('EGPCI-AAA01-0001')['Parked']
        return render(request, 'Auth/parked.html', context)

    @login_required
    def subscribers_page(request):
        context = {}
        return render(request, 'Auth/subscription.html')

    @login_required
    def user_page(request):
        if request.method == "POST":
            print(request.POST.dict())
        return render(request, 'Auth/user.html')

    @login_required
    def logout_request(request):
        logout(request)
        return redirect(reverse('logout_request'))

class authentication:
    def login(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('dashboard_page'))
            else:
                return render(request, 'Auth/login.html', {'code': 302})
        else:
            return render(request, 'Auth/login.html')

class history:
    @login_required
    def add_ticket(request):
        if request.method == "POST":
            date = request.POST.get('date')            
            time = request.POST.get('time')
            platenumber = request.POST.get('platenumber')
            models.Parkinglog.add(date, time, platenumber)
            return redirect(reverse('parked_page'))
        else:
            return(reverse('parked_page'))

    @login_required
    def close_ticket(request, ticket_id):
        pass

    
class pricing:
    @login_required
    def add_pricing(request):
        if request.method == "POST":
            fromtime = request.POST.get('fromtime')            
            totime = request.POST.get('totime')
            cost = request.POST.get('cost')
            models.Tarrif.add_tarrif(fromtime, totime, cost)
            return redirect(reverse('pricing_page'))
        else:
            return(reverse('pricing_page'))

    @login_required
    def edit_pricing(request):
        pass

    @login_required
    def delete_pricing(request):
        pass