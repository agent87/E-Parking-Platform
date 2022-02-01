from django.urls import path
from . import views


urlpatterns = [    
    path('', views.index.as_view(), name='index'),
    ###Auth Related#####
    path('login', views.authentication.login.as_view(), name='login'),
    path('logout', views.authentication.logout.as_view(), name='logout'),
    ###Register Customer#####
    path('join', views.registration.as_view() , name='registration'),

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
    path('pricing', views.pricing.as_view(), name='pricing'),

    ###Subcribers
    path('subscribers', views.subscription.subscribers_page, name='subscribers_page'),
    path('subscribers/add', views.subscription.add_subscription, name='add_subscription'), 

    path('accounts', views.responses.user_page, name='accounts_page'),
    path('accounts/add', views.users.add_user, name='add_account'),
    path('accounts/profile', views.users.self_profile, name='self_profile'),
    path('accounts/<int:user_id>/profile', views.users.user_profile, name='user_profile'),

    path('sign-up/verify-mail', views.users.verify_email_view, name='VerifyEmail'),
    path('sign-up/verify/mail/<slug:token>', views.users.verify_email_token, name='VerifyEmailToken'),
    path('sign-up/verify/mail/success', views.users.verify_email_success, name='VerifyEmailSuccess'),

    ###Settings
    path('settings', views.settings.settings_page, name='settings_page'),
    path('settings/gates/add', views.settings.add_gate, name='add_gate'),


    path('contact-us', views.contact_us.contact_us_page, name='contact_us_page'),

    #path('admin/', admin.site.urls)
]
