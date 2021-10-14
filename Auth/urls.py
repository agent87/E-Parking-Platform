from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [    
    ###Auth Related#####
    path('', views.responses.login_page, name='login_page'),
    path('login', views.responses.login_page, name='login_page'),
    path('login/<slug:redirect_to>', views.responses.login_page, name='login_page'),
    path('reset', views.responses.login_page, name='reset_page'),
    path('logout', views.responses.logout_request, name='logout_request'),

    ###Testing####
    path('test', views.responses.testing),

    ###Dashboard Related #####
    path('dashboard', views.responses.dashboard_page, name='dashboard_page'),

    ###Parking Logs Related#####
    path('history', views.responses.history_page, name='history_page'),
    path('history/<str:ticketid>', views.responses.history_page, name='history_page'),
    path('history/<str:ticketid>/del', views.responses.close_ticket, name='history_page'),
    
    path('parked', views.responses.parked_page, name='parked_page'),

    ###Tarrif Related#####
    path('pricing', views.responses.pricing_page, name='pricing_page'),

    ###Subcribers
    path('subscribers', views.responses.subscribers_page, name='subscribers_page'),

    path('users', views.responses.user_page, name='user_page'),
    path('users/enroll', views.responses.user_page, name='user_enroll_api'),
    path('admin/', admin.site.urls)
]
