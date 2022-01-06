from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [    
    ###Auth Related#####
    path('', views.LoginView.LoginView, name='LoginView'),
    path('auth/login', views.authentication.login, name='login'),
    #path('login/<slug:redirect_to>', views.responses.login_page, name='login_page'),
    path('reset', views.responses.login_page, name='reset_page'),
    path('logout', views.authentication.logout, name='logout_request'),

    ###Register Customer#####
    path('sign-up', views.Customers.RegisterView, name='RegisterView'),
    path('sign-up/submit', views.Customers.register, name='SubmitCustomerForm'),

    ###Testing####
    path('test', views.responses.testing),

    ###Dashboard Related #####
    path('dashboard', views.DashboardView.dashboard_page, name='dashboard_page'),

    ###Parking Logs Related#####
    path('history', views.history.history_page, name='history_page'),
    path('history/add', views.history.add_ticket, name='add_vehicle'),
    path('history/<slug:ticket_id>/checkout', views.history.checkout, name='checkout'),
    #path('history/<str:ticket_id>', views.responses.history_page, name='history_page'),
    path('history/<slug:ticket_id>/close', views.history.close_ticket, name='close_ticket'),
    
    ### Parked Vehicles Related#####
    path('parked', views.responses.parked_page, name='parked_page'),

    ###Tarrif Related#####
    path('pricing', views.pricing.pricing_page, name='pricing_page'),
    path('pricing/add', views.pricing.add_pricing, name='add_tarrif'),

    ###Subcribers
    path('subscribers', views.subscription.subscribers_page, name='subscribers_page'),
    path('subscribers/add', views.subscription.add_subscription, name='add_subscription'), 

    path('accounts', views.responses.user_page, name='accounts_page'),
    path('accounts/add', views.users.add_user, name='add_account'),
    path('accounts/profile', views.users.self_profile, name='self_profile'),
    path('accounts/<int:user_id>/profile', views.users.user_profile, name='user_profile'),


    path('contact-us', views.contact_us.contact_us_page, name='contact_us_page'),

    #path('admin/', admin.site.urls)
]
