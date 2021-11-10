from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [    
    ###Auth Related#####
    path('', views.responses.login_page, name='login_page'),
    path('auth/login', views.authentication.login, name='login'),
    path('login/<slug:redirect_to>', views.responses.login_page, name='login_page'),
    path('reset', views.responses.login_page, name='reset_page'),
    path('logout', views.responses.logout_request, name='logout_request'),

    ###Testing####
    path('test', views.responses.testing),

    ###Dashboard Related #####
    path('dashboard', views.responses.dashboard_page, name='dashboard_page'),

    ###Parking Logs Related#####
    path('history', views.responses.history_page, name='history_page'),
    path('history/add', views.history.add_ticket, name='add_vehicle'),
    path('history/<str:ticketid>', views.responses.history_page, name='history_page'),
    path('history/<slug:ticketid>/close', views.responses.close_ticket, name='close_ticket'),
    
    path('parked', views.responses.parked_page, name='parked_page'),

    ###Tarrif Related#####
    path('pricing', views.responses.pricing_page, name='pricing_page'),
    path('pricing/add', views.pricing.add_pricing, name='add_tarrif'),

    ###Subcribers
    path('subscribers', views.responses.subscribers_page, name='subscribers_page'),
    path('subscribers/add', views.responses.subscribers_page, name='add_subscriber'), 

    path('users', views.responses.user_page, name='user_page'),
    path('users/add', views.responses.user_page, name='add_user'),
    path('admin/', admin.site.urls)
]
