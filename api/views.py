from flask import Flask, Response, abort, request, json, jsonify
from .models import JSON_MIME_TYPE, Ride,User
from .models import c

app = Flask(__name__)


@classmethod 
@app.route('/rides', methods=["GET"])
def get_all_rides():    
    cur = c.cursor()
    response = ''
    query = 'SELECT * FROM rides'
    if cur is not None:
        cur.execute(query)
        c.commit()
        rows = cur.fetchall()
        response = json.dumps(rows)
    return response, 200


@classmethod 
@app.route('/rides/<ride_id>', methods=["GET"])
def get_ride(ride_id):
    cur = c.cursor()
    response = ''
    query = ("SELECT * FROM rides WHERE ride_id ='{}'".format(ride_id))
    if cur is not None:
        cur.execute(query)
        c.commit()
        rows = cur.fetchone()
        response = json.dumps(rows)
    return response, 200


@classmethod #converts ftn to class method
@app.route('/users/rides',methods=['POST'])
def create_ride():
    data = request.get_json()
    
    ride = Ride(data['ride_id'], data['d_name'], data['origin'], data['departure_time'],  data['destination'],  
                data['cost'], data['ride_status'])
    response = Ride.post_ride(ride)
    result ="Ride Created"
    return jsonify({"Message":result}),201


@app.route('/auth/signup', methods=['POST'])
def register():
    try:
        data = request.get_json()
        user = User(data['username'], data['email'], data['password'])
        result = User.post_user(user)
        result = "User Created"
        return jsonify({"Message":result}),201
    except:
        return jsonify("Message :User with same email exists!"),500
 

@app.errorhandler(404)
def not_found(e):
    return 'Ride Not Found', 404

@app.errorhandler(400)
def ride_duplicate(e):
    return 'Same Ride Exists', 400
