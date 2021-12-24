from SystemApp import models
from SystemApp import managers
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import time


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
                return render(request, 'DashboardApp/Authentication/login.html', {'code': 302})
        else:
            return render(request, 'DashboardApp/Authentication/login.html')

    
    def testing(request):
        return render(request, 'Auth/histor.html')

    

    @login_required
    def parked_page(request):
        context = {'parked_vehicles' : models.Parkinglog.objects.filter(customer_id=request.user.customer_id.customer_id, parked=True)}
        context['EntranceFormContext'] = {'gates' : models.Gates.objects.filter(customer_id=request.user.customer_id.customer_id)}
        return render(request, 'DashboardApp/ParkingLogs/ParkedVehicles.html', context)

    @login_required
    def subscribers_page(request):
        print(request.user.customer_id.customer_id)
        context = {"subscription" : models.Subscriptions.objects.filter(customer_id = request.user.customer_id.customer_id)}
        context['user'] = request.user
        return render(request, 'DashboardApp/Subscribers/subscription.html', context)

    @login_required
    def user_page(request):
        context = {'users': models.Users.objects.filter(customer_id = request.user.customer_id.customer_id)}
        context['user'] = request.user
        return render(request, 'DashboardApp/Accounts/user.html', context)

    @login_required
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

    def logout(request):
        logout(request)
        return redirect(reverse('LoginView'))

class RegisterView:
    def RegisterView(request):
        return render(request, 'DashboardApp/Accounts/CustomerForm.html')


class DashboardView:
    @login_required
    def dashboard_page(request):
        context = {'parking_logs' : models.Parkinglog.objects.filter(customer_id=request.user.customer_id.customer_id)}
        context['gates'] = models.Gates.objects.filter(customer_id=request.user.customer_id.customer_id)
        context['subscription'] = models.Subscriptions.objects.filter(customer_id = request.user.customer_id.customer_id)
        context['user'] = request.user
        context['customer'] = request.user.customer_id
        return render(request, 'DashboardApp/Dashboard/dashboard.html', context)

class LoginView:
    def LoginView(request):
        return render(request, 'DashboardApp/Authentication/login.html')


class history:
    @login_required
    def history_page(request):
        context = {'parking_logs': models.Parkinglog.objects.filter(customer_id=request.user.customer_id.customer_id)}
        context['user'] = request.user
        return render(request, 'DashboardApp/ParkingLogs/HistoryPage.html', context)

    @login_required
    def add_ticket(request):
        if request.method == "POST":
            customer_id = request.user.customer_id.customer_id
            date = request.POST.get('date')            
            time = request.POST.get('time')
            plate_number = request.POST.get('platenumber')
            gate_id = request.POST.get('gate')
            user_id = request.user.user_id
            models.Parkinglog.add(customer_id, date, time, plate_number, gate_id, user_id, checkin_method='Manual')
            return redirect(reverse('parked_page'))
        else:
            return(reverse('parked_page'))

    @login_required
    def checkout(request, ticket_id):
        context = {'ticket' : models.Parkinglog.objects.get(ticket_id=ticket_id)}
        context['gates'] = models.Gates.objects.filter(customer_id=context['ticket'].customer_id.customer_id)
        context['user'] = request.user
        context['cost'] = models.Tarrif.match_tarrif(context['ticket'].elapsed).cost
        context['subscription'] = models.Subscriptions.is_subscribed(plate_number = context['ticket'].plate_number)
        return render(request, 'DashboardApp/ParkingLogs/CheckoutForm.html', context)

    @login_required
    def close_ticket(request, ticket_id):
        models.Parkinglog.close(ticket_id = ticket_id, 
                                checkin_time = request.POST.get('checkin_datetime'),
                                checkout_time = request.POST.get('checkout_datetime'),
                                checkout_method='Manual',
                                checkout_user = request.user.user_id,
                                exit_gate = request.POST.get('exit_gate'), 
                                amount_payed = request.POST.get('amount_payed'),
                                payment_method = request.POST.get('payment_method')
                                )
        return redirect(reverse('parked_page'))

    
class pricing:
    @login_required
    def pricing_page(request):
        context = {'tarrifs' : models.Tarrif.objects.all()}
        context['user'] = request.user
        return render(request, 'DashboardApp/Pricing/PricingPage.html', context)

    @login_required
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

    @login_required
    def edit_pricing(request):
        pass

    @login_required
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
            return redirect(reverse('accounts_page'))
        else:
            return redirect(reverse('accounts_page'))

    @login_required
    def self_profile(request):
        context = {'user_profile': request.user}
        return render(request, 'DashboardApp/Accounts/Profile.html', context)

    @login_required
    def user_profile(request, user_id):
        context = {'user_profile': models.Users.objects.get(user_id=user_id)}
        context['user'] = request.user
        return render(request, 'DashboardApp/Accounts/Profile.html', context)

    

class subscription:
    @login_required
    def subscribers_page(request):
        print(request.user.customer_id.customer_id)
        context = {"subscriptions" : models.Subscriptions.objects.filter(customer_id = request.user.customer_id.customer_id)}
        return render(request, 'DashboardApp/Subscribers/subscription.html', context)

    @login_required
    def add_subscription(request):
        if request.method == "POST":
            user_id = request.user.user_id
            customer_id = request.user.customer_id.customer_id
            platenum = request.POST.get('platenum')
            name = request.POST.get('name')
            phonenum = request.POST.get('phonenum')
            office = request.POST.get('office')
            parklot = request.POST.get('parklot')
            amount = request.POST.get('amount')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            models.Subscriptions.add_subscription(user_id, customer_id, platenum, name, phonenum, office, parklot, amount, start_date, end_date)
            return redirect(reverse('subscribers_page'))
        else:
            return redirect(reverse('subscribers_page'))


class contact_us:
    def contact_us_page(request):
        return render(request, 'DashboardApp/Accounts/contact-us.html')

    def send_message(request):
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            #models.ContactUs.add_message(name, email, message)
            return redirect(reverse('contact_us_page'))
        else:
            return redirect(reverse('contact_us_page'))