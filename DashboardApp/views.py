from django.http import HttpResponseBadRequest, JsonResponse
from DashboardApp.forms import LoginForm
from SystemApp import models
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from DashboardApp import forms
import json


class index(View):
    def get(self, request):
        return redirect(reverse('login'))

class registration(View):
    template = 'DashboardApp/Accounts/CustomerForm.html'
    context = { 'CustomerForm': forms.CustomerForm() }
    context['AdminForm'] = forms.UserForm()

    def get(self, request):
        return render(request, self.template, context=self.context)

    def post(self, request):
        Customer = forms.CustomerForm(request.POST)
        Admin = forms.UserForm(request.POST)
        if Customer.is_valid() and Admin.is_valid():
            if models.Users.objects.filter(email=Admin.cleaned_data['email']).exists():
                Admin.add_error(None, "Admin email already exists")
                self.context['CustomerForm'] = Customer
                self.context['AdminForm'] = Admin
                self.context['FormError'] = Admin.errors.get_json_data()['__all__']
                return render(request, self.template, context=self.context)
            else:
                customer_id = models.Customers.enroll(Customer).customer_id
                models.Users.enroll(customer_id, Admin, role="Admin")
                return redirect(reverse('VerifyEmail'))
        else:
            self.context['CustomerForm'] = Customer.add_error(None, "Please fill all the fields & check for errors")
            self.context['AdminForm'] = Admin
            return render(request, self.template, context=self.context)

class authentication:
    class login(View):
        template = 'DashboardApp/Authentication/login.html'
        context = {'LoginForm': LoginForm()}

        def get(self, request):
            self.context['LoginForm'] = LoginForm()
            return render(request, self.template, context=self.context)

        def post(self, request):
            form = LoginForm(request.POST)
            if form.is_valid():
                user = auth.authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
                if user is not None:
                    auth.login(request, user)
                    return redirect(reverse('dashboard_page'))
                else:
                    form.add_error(None, "Incorect email or password!")
                    self.context['LoginForm'] = form
                    self.context['errors'] = form.errors.get_json_data()['__all__']
                    return render(request, self.template, context=self.context)
            else:
                form.add_error(None, "Please fill all the fields & check for errors")
                self.context['LoginForm'] = form
                self.context['errors'] = form.errors.get_json_data()['__all__']
                return render(request, self.template, context=self.context)
        
    class logout(View):
        def get(request):
            auth.logout(request)
            return redirect(reverse('LoginView'))
    
class pricing(LoginRequiredMixin, View):
    template_name = 'DashboardApp/Pricing/PricingPage.html'
    context = {'tarrifForm' : forms.TarrifForm()}
    http_method_names = ['get', 'post']

    def get(self, request):
        self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
        self.context['user'] = request.user
        return render(request, self.template_name, self.context)

    def post(self, request):
        if request.POST.get('action') == 'add':
            form = forms.TarrifForm(request.POST)
            if form.is_valid():
                form.cleaned_data['customer_id'] = request.user.customer_id
                form.create()
                self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
                self.context['success'] = {'message': 'Tarrif updated successfully'}
                return render(request, self.template_name, self.context)
            else:
                self.context['tarrifForm'] = form
                self.context['errors'] = form.errors.get_json_data()
                return render(request, self.template_name, self.context)

        elif request.POST.get('action') == 'update':
            form = forms.TarrifForm(request.POST)
            if form.is_valid():
                form.update()
                self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
                self.context['success'] = {'message': 'Tarrif updated successfully'}
                return render(request, self.template_name, self.context)
            else:
                self.context['tarrifForm'] = form
                self.context['errors'] = form.errors.get_json_data()
                return render(request, self.template_name, self.context)

        elif request.POST.get('action') == 'delete':
            tarrif_id = request.POST.get('tarrif_id')
            models.Tarrif.objects.get(tarrif_id=tarrif_id).delete()
            self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
            return render(request, self.template_name, self.context)

        else:
            return HttpResponseBadRequest()


 
class parking(LoginRequiredMixin, View):
    template_name = 'DashboardApp/ParkingLogs/Parking.html'
    context = {}

    def get(self, request):
        if request.GET.get('format') == 'json':
            if request.GET.get('ticket_id'):
                ticket_id = int(request.GET.get('ticket_id'))
                ticket_obj = models.Parkinglog.objects.filter(ticket_id=ticket_id, customer_id=request.user.customer_id.customer_id)
                if ticket_obj.exists():
                    ticket_json = {'fields' :json.loads(serializers.serialize('json', [ticket_obj[0],]))[0]['fields']}
                    print(ticket_json)
                    return JsonResponse(ticket_json, safe=False)
                else:
                    return JsonResponse({'error': 'No such ticket exists'})
            else:
                return HttpResponseBadRequest("Please provide a ticket id")

        else:
            self.context['CheckinForm'] = forms.TicketForm.CheckinForm()
            self.context['CheckinForm'].populate(request.user.customer_id.customer_id)
            self.context['CheckoutForm'] = forms.TicketForm.CheckoutForm()
            self.context['alerts'] = None
            self.context['vehicles'] = models.Parkinglog.objects.filter(customer_id=request.user.customer_id.customer_id)
            self.context['user'] = request.user
            return render(request, self.template_name, self.context)

    def post(self, request):
        self.request = request
        if request.POST.get('action') == 'add':
            form = forms.TicketForm.CheckinForm(request.POST)
            if form.is_valid():
                if models.Parkinglog.objects.filter(customer_id=request.user.customer_id.customer_id, plate_number=form.cleaned_data['plate_number'], parked = True).exists():
                    self.context['alerts'] = [{'message': 'Vehicle already parked! Consider checking out the vehicle.', 'title':'Vehicel already parked', 'type':'error'},]
                    self.context['vehicles'] = models.Parkinglog.objects.filter(customer_id=request.user.customer_id.customer_id)
                    return render(request, self.template_name, self.context)
                else:
                    form.cleaned_data['user'] = request.user
                    form.create()
                    self.context['vehicles'] = models.Parkinglog.objects.filter(customer_id=request.user.customer_id.customer_id)
                    self.context['alerts'] = [{'message': f"Ticket with vehicle plate number {form.cleaned_data['plate_number']} has been added sucessfully.", 'title':'Vehicle added succesffuly', 'type':'success'}]
                    return render(request, self.template_name, self.context)
            else:
                self.context['parkingForm'] = form
                self.context['errors'] = form.errors.get_json_data()
                return render(request, self.template_name, self.context)

        elif request.POST.get('action') == 'update':
            form = forms.TicketForm.CheckinForm(request.POST)
            if form.is_valid():
                form.update()
                self.context['vehicles'] = models.Parkinglog.objects.filter(customer_id=request.user.customer_id.customer_id)
                self.context['success'] = {'message': 'Vehicle updated successfully'}
                return render(request, self.template_name, self.context)
            else:
                self.context['parkingForm'] = form
                self.context['errors'] = form.errors.get_json_data()
                return render(request, self.template_name, self.context)

        elif request.POST.get('action') == 'delete':
            ticket_id = request.POST.get('item_id')
            obj =  models.Parkinglog.objects.filter(ticket_id=ticket_id, customer_id=request.user.customer_id.customer_id)
            if obj.exists(): 
                plate_number = obj.first().plate_number
                obj.delete()
                self.context['alerts'] = [{'message': f"Ticket with with Plate number {plate_number} has been removed.", 'title':'Ticket removed successfully', 'type':'success'}]
                self.context['vehicles'] = models.Parkinglog.objects.filter(customer_id=request.user.customer_id.customer_id)
                return render(request, self.template_name, self.context)
            else:
                self.context['alerts'] = [{'message': 'Unable to find ticket with matching plate number', 'title':'Invalid request', 'type':'error'},]
                self.context['vehicles'] = models.Parkinglog.objects.filter(customer_id=request.user.customer_id.customer_id)
                return render(request, self.template_name, self.context)

        else:
            return HttpResponseBadRequest()

class subscription(LoginRequiredMixin, View):
    template_name = "DashboardApp/Subscribers/Subscriptions.html"
    context = {'context' : forms.SubscriptionForm }

    def get(self, request):
        self.context['subscribers'] = models.Subscriptions.objects.filter(customer_id=request.user.customer_id.customer_id)
        return render(request, self.template_name, self.context)

    def post(self, request):
        return render(request, self.template_name, self.context)



# Create your views here.
class responses:
    def login_page(request, redirect_to=None):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(request, username=username, password=password)
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
        auth.logout(request)
        return redirect(reverse('logout_request'))

class Customers:
    def RegisterView(request):
        return render(request, 'DashboardApp/Accounts/CustomerForm.html')


    def register(request):
        try:
            customer = models.Customers.enroll_customer(company_name=request.POST.get('customer_name'), address = request.POST.get('address'))
            if customer[0]:
                try:
                    User = models.Users.add_user(customer[1].customer_id, request.POST.get('first_name'), request.POST.get('last_name'), request.POST.get('email'), request.POST.get('phonenum'), request.POST.get('password'), 'Admin')
                    if User[0]:
                        return redirect(reverse('VerifyEmail'))
                    else:
                        return redirect(reverse('RegisterView'))
                except ObjectDoesNotExist:
                    return redirect(reverse('RegisterView'))
        
        except ObjectDoesNotExist:
            return redirect(reverse('RegisterView'))
    


class DashboardView:
    @login_required
    def dashboard_page(request):
        context = {'parking_logs' : models.Parkinglog.objects.filter(customer_id=request.user.customer_id.customer_id)}
        context['gates'] = models.Gates.objects.filter(customer_id=request.user.customer_id.customer_id)
        context['subscription'] = models.Subscriptions.objects.filter(customer_id = request.user.customer_id.customer_id)
        context['user'] = request.user
        context['customer'] = request.user.customer_id
        context['payements_summary'] = models.Customers.objects.get(customer_id = request.user.customer_id.customer_id).payements_summary
        return render(request, 'DashboardApp/Dashboard/dashboard.html', context)



class history:
    @login_required
    def history_page(request):
        context = {'parking_logs': models.Parkinglog.objects.filter(customer_id=request.user.customer_id.customer_id)}
        context['user'] = request.user
        return render(request, 'DashboardApp/ParkingLogs/HistoryPage.html', context)

    

    @login_required
    def checkout(request, ticket_id):
        context = {'ticket' : models.Parkinglog.objects.get(ticket_id=ticket_id)}
        context['gates'] = models.Gates.objects.filter(customer_id=context['ticket'].customer_id.customer_id)
        context['user'] = request.user
        context['cost'] = models.Tarrif.match_tarrif(context['ticket'].elapsed)
        context['subscription'] = models.Subscriptions.is_subscribed(customer_id=request.user.customer_id.customer_id, plate_number = context['ticket'].plate_number)
        return render(request, 'DashboardApp/ParkingLogs/CheckoutForm.html', context)

    

       

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

    def verify_email_view(request):
        return render(request, 'DashboardApp/Accounts/verify-mail.html')

    def verify_email_token(request, token):
        try:
            verify_mail = models.Users.objects.get(mail_verified=token)
            verify_mail.mail_verified = True
            verify_mail.save()
            return redirect(reverse('VerifyEmailSuccess'))
        except models.Users.DoesNotExist:
            return redirect(reverse('VerifyEmail'))

    def verify_email_success(request):
        return render(request, 'DashboardApp/Accounts/success-mail.html')
 
class settings:
    @login_required
    def settings_page(request):
        context = {'user' : request.user}
        context['gates'] = models.Gates.objects.filter(customer_id=request.user.customer_id.customer_id)
        return render(request, 'DashboardApp/Settings/settings.html', context)
    
    @login_required
    def add_gate(request):
        if request.method == "POST":
            customer_id = request.user.customer_id
            name = request.POST.get('gate_name')
            status = request.POST.get('status')
            models.Gates.add_gate(customer_id, name, status)
            return redirect(reverse('settings_page'))
        else:
            return redirect(reverse('settings_page'))

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