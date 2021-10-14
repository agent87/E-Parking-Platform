import cv2
from tracker import *
from vehicle_detector import VehicleDetector
import requests
import psycopg2
import time
import datetime

# Load Veichle Detector
vd = VehicleDetector()

conn = psycopg2.connect(database="d7pibsdo79jogi",host="ec2-52-86-25-51.compute-1.amazonaws.com",port=5432,user="cccbiffnldwfkf",password="605444bcd83d702da6e7f56cb2fba0ebb74fb3db14dc5a0c1555bbfa75a357a1")
cur = conn.cursor()

# Create tracker object
tracker = EuclideanDistTracker()

cap = cv2.VideoCapture('highway.mp4')
vehicles_folder_count = 0

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

def parking_log(Plate):
    #Check if the Plate is already in the database & Parked
    cur.execute(f""" select * from public."Auth_parkinglog" where "CustomerId" = 'EGPCI-AAA01-0001' and "PlateNum" = '{Plate}' and "Status" = 'Parked';""")
    query = cur.fetchall()
    if query:
        elapsed = (time.time()- query[0][5]) /60
        if elapsed <= 30:
            cash = 300
        elif elapsed <= 60:
            cash  = 500
        elif elapsed <= 90:
            cash = 700
        else:
            cash = 1000
        
        #update Checkoutimte, status, cost  and duration
        cur.execute(f""" UPDATE public."Auth_parkinglog" SET "CheckoutTime"= {time.time()}, "ExitGateId"='Main', "Status"='Exited', "Duration"={elapsed}, "Cash"={cash} WHERE "TicketId"=uuid'{query[0][0]}'; """)
        conn.commit()
    else:
        cur.execute(f"""INSERT INTO public."Auth_parkinglog" ("TicketId", "CustomerId", "Date", "PlateNum", "EntryGateId", "CheckinTime", "CheckoutTime", "ExitGateId", "Status", "Duration", "Cash") VALUES(uuid'{uuid.uuid4()}', 'EGPCI-AAA01-0001', date'{str(datetime.datetime.now().date())}', '{Plate}','Main', {time.time()}, Null, Null, 'Parked', Null, Null);""")
        conn.commit()
    #If it is then update the time stamp, Exit Gate, Status & duration
    #else add the Plate to the database

def alpr(img):
    regions = ['in']
    response = requests.post('https://api.platerecognizer.com/v1/plate-reader/',
                                data=dict(regions=regions),  # Optional
                                files=dict(upload=img),
                                headers={'Authorization': 'Token ec549d56a1930e6da1cbe3dccda9910bcb54072a'})
    resp_json = response.json()
    print(resp_json)
    try:
        Plate = str(resp_json['results'][0]['plate']).upper()
        parking_log(Plate)
        exit()
    except IndexError:
        print("No Plate Detected")

while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape
    print(height, width)

    # Extract Region of i  nterest
    roi = frame[100: 430,200: 600]
    vehicle_boxes = vd.detect_vehicles(frame)
    vehicle_count = len(vehicle_boxes)

    # Update total count
    vehicles_folder_count += vehicle_count

    for box in vehicle_boxes:
        x, y, w, h = box

        cv2.rectangle(frame, (x, y), (x + w, y + h), (25, 0, 180), 3)

        cv2.putText(frame, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

        cv2.imshow("Cars", frame)
        cv2.waitKey(1)
    retval, buffer = cv2.imencode('.jpeg', frame)
    #jpg_as_text = base64.b64encode(buffer)
    if vehicle_count > 0:
        alpr(buffer)
    
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()