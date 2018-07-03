'''
Auther:Okello Gabriel Innocent
Profession: Software Developer
'''
from flask import Flask, abort, request
from flask_restful import Resource, Api
from .models import rides
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