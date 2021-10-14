from . import models
from datetime import datetime
from django.utils import timezone
import time

class dashboard:
    def compile(customerid):
        context = {}
        models.Parkinglog.objects.filter(customerid=customerid)

        return context



class ParkingLog:
    def compile(customerid):
        Logs = models.Parkinglog.objects.all()
        context = {
            'History' : {'Count' : Logs.count(), 
                         'List': ParkingLog.History_list(Logs)},
            'Today' : {'Cars' : Logs.filter(date=timezone.now()).count(), 
                       'Revenue': ParkingLog.Today_revenue(Logs)},
            'Parked' : {'Now': Logs.filter(status='Parked').count(), 
                        'List': ParkingLog.Parked_list(Logs)}

                    }

        return context

    def History_list(logs):
        History_list = []
        for log in logs:
            item = {'TicketId': log.ticketid}
            item['Date'] = str(log.date)
            item['PlateNum'] = log.platenum
            item['EntryGate'] = log.entrygateid
            item['Checkin'] = datetime.utcfromtimestamp(log.checkintime).strftime('%H:%M:%S')
            item['Checkout'] = datetime.utcfromtimestamp(log.checkouttime).strftime('%Y-%m-%d %H:%M:%S') if log.checkouttime else None
            item['ExitGate'] = log.exitgateid
            item['Status'] = log.status
            item['Duration'] = log.duration
            item['Cash'] = log.cash
            History_list.append(item)

        return History_list

    def Parked_list(logs):
        Today_list = []
        for log in logs.filter(status='Parked'):
            item = {'TicketId': str(log.ticketid)}
            item['Date'] = str(log.date)
            item['PlateNum'] = log.platenum
            item['EntryGate'] = log.entrygateid
            item['Checkin'] = datetime.utcfromtimestamp(log.checkintime).strftime('%H:%M:%S')
            item['Status'] = log.status
            item['Duration'] = int((time.time() - log.checkintime) / 60)
            item['Cash'] = log.cash
            Today_list.append(item)

        return Today_list

    def Today_revenue(logs):
        Today_revenue = 0
        for log in logs.filter(status='Exited'):
            Today_revenue += int(log.cash)

        return Today_revenue





    