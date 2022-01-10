import requests
from django.core.mail import send_mail
from django.conf import settings
import os


def time_str(time_int):
    #recieve time in seconds int
    if time_int < 60:
        return f'0 Minutes'

    else:
        intervals = (
        ('weeks', 604800),  # 60 * 60 * 24 * 7
        ('days', 86400),    # 60 * 60 * 24
        ('hours', 3600),    # 60 * 60
        ('minutes', 60),
        ('seconds', 1),)
        result = []
        granularity=1
        for name, count in intervals:
            value = round(time_int // count)
            if value:
                time_int -= value * count
                if value == 1:
                    name = name.rstrip('s')
                result.append("{} {}".format(value, name))
        return f'{result[0]}'


class mail_server:
    def send(subject, message, recipient_list):
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

class sms_server:
    def send_sms(message, recipient_list):
        data= {'recipients':f'{recipient_list}', 'message':message, 'sender':f'{os.environ.get("SMS_SENDER_NUMBER")}'}
        r = requests.post('https://www.intouchsms.co.rw/api/sendsms/.json',  data,  auth=(os.environ.get('SMS_API_USERNAME'), os.environ.get('SMS_API_PASSWORD')))

        return r.status_code

    def subscription_reciept(recipient, recipient_name, plate_number, valid_until, amount, parking_operator_name):
        message = f'Hello {recipient_name}, your parking subscription for vehicle with {plate_number} is valid until {valid_until}. Amount paid is {amount} Rwf. Thank you for using our service. Ewawe-parking'
        r =  sms_server.send_sms(message, recipient)
        return r