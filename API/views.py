from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from requests.api import request
import SystemApp
import datetime
from uuid import uuid4


class ParkingLogs:
    @csrf_exempt
    def Post(request):
        if request.method == 'POST':
            if request.POST.get('flow') == 'entry':
                ticket_id = uuid4()
                SystemApp.models.Parkinglog.objects.create(plate_number=request.POST.get('plate_number'), 
                                    date = datetime.datetime.now(),
                                    ticket_id = ticket_id,
                                    customer_id = SystemApp.models.Customers.objects.get(customer_id=request.POST.get('customer_id')),
                                    checkin_time= int(float(request.POST.get('time'))),
                                    checkin_method = 'Camera',
                                    entry_gate= SystemApp.models.Gates.objects.get(gate_id=request.POST.get('gate')),
                                    parked = True)
        
                try:
                    SystemApp.models.Parkinglog.objects.filter(ticket_id=ticket_id).update(subscription=SystemApp.models.Subscriptions.objects.get(plate_number=request.POST.get('plate_number')))
                except ObjectDoesNotExist:
                    pass
                response = HttpResponse()
                response['TicketId'] = ticket_id
                return response

            else:
                response = HttpResponse()
                response['TicketId'] = 200
                return response
        else:
            return None