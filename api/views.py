import json
from flask import Flask, Response, abort
from .models import JSON_MIME_TYPE, Ride

app = Flask(__name__)
data = request.json()

@app.route('/api/v1/rides')
def get_all_ride():    
    response = Ride.get_rides(data)
    return  jsonify({'response':usr}),200


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
def create_ride(data):
    response =Ride.post_ride(data)
    return response

'''@app.route('/api/v1/rides/<ride_id>/requests', methods=['POST',])
def request_to_join_ride(ride_id):
        for ride in rides:
            if ride['ride_id']:
                ride['status'] == True
                rides.append(ride)
                return "A request has been sent"

@app.route('/api/v1.0/tasks/<ride_id>', methods=['PUT'])

'''
@app.errorhandler(404)
def not_found(e):
    return 'Ride Not Found', 404