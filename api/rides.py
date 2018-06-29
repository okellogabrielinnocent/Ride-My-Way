'''
Auther:Okello Gabriel Innocent
Profession: Software Developer
'''
from flask import Flask, abort, request
from flask_restful import Resource, Api
from .views import rides
from .models import Ride


app = Flask(__name__)
api = Api(app)

LAST_ID = 33


class RideResource(Resource):
    def get(self, ride_id):
        ride = Ride.get_ride(ride_id)
        if ride is None:
            abort(404)
        return ride
    
class RideListResource(Resource):
    def get(self):
        return rides

    def post(self):
        global LAST_ID
        LAST_ID += 1
        
        ride = {
            'id':LAST_ID,
            'd_name':request.json['d_name'],
            'departure_time':request.json['departure_time'],
            'origin':request.json['origin'],
            'destination':request.json['destination'],
            'cost':request.json['cost'],
            'status':"True"
            }
        rides.append(ride)
        return ride, 201