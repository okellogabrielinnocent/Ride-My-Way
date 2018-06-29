import json
from flask import Flask, Response, abort
from .models import JSON_MIME_TYPE, Ride

app = Flask(__name__)

rides = [{
        'ride_id':'1',
        'd_name':'Gabriel',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':"False"
        },
        {
        'ride_id':'2',
        'd_name':'Okello',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':"True"
        },
        {
        'ride_id':3,
        'd_name':'Innocent',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':"True"
        },
        {
        'ride_id':'4',
        'd_name':'Susan',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':"True"
        },
        {
        'ride_id':'5',
        'd_name':'Abram',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':"True"
        },
        {
        'ride_id':'6',
        'd_name':'Eunice',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':"True"
        }]


@app.route('/api/v1/rides')
def getAllride():
    response = Response(
        json.dumps(rides), status=200, mimetype=JSON_MIME_TYPE)
    return response


@app.route('/api/v1/rides/<ride_id>')
def get_ride(ride_id):
    ride = Ride.get_ride(ride_id)
    if ride is None:
        abort(404)

    content = json.dumps(ride)
    return content, 200, {'Content-Type': JSON_MIME_TYPE}

@classmethod 
    #converts ftn to class method
@app.route('/api/v1/rides',methods=['POST'])
def create_ride(ride_id):
    ride =Ride.get_ride(ride_id)
#check if ride already exists
    for ride in rides:
            if ride['ride_id'] == ride_id:
                return  "Ride already exists"
        
    content = json.dumps(ride)
    return content, 201, {'Content-Type': JSON_MIME_TYPE}

@app.route('/api/v1/rides/<ride_id>/requests', methods=['POST',])
def request_to_join_ride(ride_id):
        for ride in rides:
            if ride['id']:
                ride['status'] == True
                rides.append(ride)
                return "A request has been sent"

@app.errorhandler(404)
def not_found(e):
    return 'Ride Not Found', 404